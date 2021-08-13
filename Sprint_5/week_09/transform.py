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

def organize_date_values(df):
    df2 = df.filter(df.created_at > '2018-01-01')\
                    .filter(df.created_at < '2020-01-01')
    return df2

def import_csv(spark, src):
    tweets = t.StructType([
        t.StructField("id", t.LongType(), False),
        t.StructField("text", t.StringType(), False),
        t.StructField("created_at", t.TimestampType(), False)
    ])
    #IMPORTACAO S3 - Apenas colocando a URI do bucket
    if src is not None:
        df = spark.read.option("quotes", "\"").option("escape", "\"").schema(tweets).csv(src)
    return df

def export_parquet(df, dest):
    df.write.mode("overwrite").partitionBy("created_date").parquet(dest)


def twitter_transform(src, dest):
    with SparkSession.builder.appName("Twitter Transformation").getOrCreate() as spark:
        df = import_csv(spark, src)
        df2 = organize_date_values(df)
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