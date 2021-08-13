import argparse
from pyspark.sql import SparkSession
from pyspark.sql import functions as f
from pyspark.sql import types as t

def create_columns_data(df):
    
    df2 = df\
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
    return df2

def preprocessing(df):
    df = df.withColumn('text', f.regexp_replace('text', r'http\S+', ''))
    df = df.withColumn('text', f.regexp_replace('text', '@\w+', ''))
    df = df.withColumn('text', f.regexp_replace('text', '#', ''))
    df = df.withColumn('text', f.regexp_replace('text', 'RT', ''))
    df = df.withColumn('text', f.regexp_replace('text', ':', ''))

    df = df.withColumn("source", 
        f.when(df.source.contains("Twitter for Android"), "Android")
        .when(df.source.contains("Twitter for Iphone"), "IOS")
        .when(df.source.contains("Twitter for iPad"), "IOS")
        .when(df.source.contains("Twitter Web App"), "Web")
        .otherwise(""))

    df = df.na.replace('', None)
    df = df.na.drop()
    return df

def import_json(spark, src):
    tweets = t.StructType([
        t.StructField("id", t.LongType(), False),
        t.StructField("text", t.StringType(), False),
        t.StructField("created_at", t.TimestampType(), False),
        t.StructField("source", t.StringType(), False),
        t.StructField("retweets", t.StringType(), False)
    ])

    df = spark \
        .readStream\
        .schema(tweets) \
        .option("multiline", 'true')\
        .json(src)

    return df

def export_parquet(df, dest):
    df.repartition(f.window(df.created_at, "15 minutes", "5 minutes"))
    query = df\
        .writeStream\
        .outputMode("append").format("parquet")\
        .partitionBy('created_date')\
        .option("path", dest + "/results")\
        .option("checkpointLocation", dest + "/checkpoint")\
        .trigger(processingTime='15 minutes')\
        .start()
    query.exception()
    query.awaitTermination()



def twitter_transform(src, dest):
    with SparkSession.builder.appName("Twitter Transformation").getOrCreate() as spark:
        df = import_json(spark, src)
        df2 = preprocessing(df)
        df3 = create_columns_data(df2)
        export_parquet(df3, dest)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Spark Twitter Transformation"
    )
    parser.add_argument("--src", required=True)
    parser.add_argument("--dest", required=True)
    args = parser.parse_args()

    twitter_transform(args.src, args.dest)