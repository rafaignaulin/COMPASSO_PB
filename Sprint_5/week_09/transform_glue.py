import sys
from pyspark.context import SparkContext
from pyspark.sql import SparkSession
from pyspark.sql import functions as f
from pyspark.sql import types as t

from awsglue.utils import getResolvedOptions
from awsglue.context import GlueContext
from awsglue.dynamicframe import DynamicFrame
from awsglue.job import Job

args = getResolvedOptions(sys.argv, ['JOB_NAME'])

spark_context = SparkContext.getOrCreate()
glue_context = GlueContext(spark_context)
session = glue_context.spark_session

job = Job(glue_context)
job.init(args['JOB_NAME'], args)

#Read movie data to Glue dynamic frame
dynamic_frame_read = glue_context.create_dynamic_frame.from_catalog(database = 'xpto', table_name = 'twitter_raw_csv')

#Convert dynamic frame to data frame to use standard pyspark functions
df = dynamic_frame_read.toDF()

#Arrumar Schema inicial
df = df.select(df.col0.alias('id'), df.col1.alias('text'), f.to_timestamp(df.col2, "yyyy-MM-dd HH:mm:ss").alias('created_at'))

#Filtrar Bad Data
df2 = df.filter(df.created_at > '2018-01-01')\
        .filter(df. created_at  < '2020-01-01')

#Adicionar novas colunas
df3 = df2\
    .withColumn("created_date", f.to_date("created_at")).repartition("created_date")\
    .withColumn("sentimento", 
        f.when((df.text.contains(":D")) | (df.text.contains(":)")) | (df.text.contains(":]")) | (df.text.contains(":P")), "Positivo")
        .when((df.text.contains("D:")) | (df.text.contains(":(")) | (df.text.contains(":[")), "Negativo")
        .otherwise("Neutro"))\
    .withColumn("simbolo", 
        f.when(df.text.contains(":D"), ":D")
        .when(df.text.contains(":)"), ":)")
        .when(df.text.contains(":]"), ":]")
        .when(df.text.contains(":P"), ":P")
        .when(df.text.contains("D:"), "D:")
        .when(df.text.contains(":("), ":(")
        .when(df.text.contains(":["), ":[")
        .otherwise(":|"))

# WRITE TO S3 PATH
df_tweets_write = DynamicFrame.fromDF(df3, glue_context,"df_tweets_write")
glue_context.write_dynamic_frame.from_options(
    frame = df_tweets_write,
    connection_type = "s3",
    connection_options = {
    "path": 's3://xpto-refined/batch/',
    "partitionKeys": ["created_date"]
    },format = "parquet")

job.commit()