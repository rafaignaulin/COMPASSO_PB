from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pyspark.sql import functions as F

spark = SparkSession.builder.appName("TwitterSentimentAnalysis").getOrCreate()

tweets = spark.readStream.format("socket").option("host", "0.0.0.0").option("port", 5555).load()

tweets = tweets.repartition(1)

query = tweets.writeStream.queryName("all_tweets")\
    .outputMode("append").format("csv")\
    .option("path", "./parc")\
    .option("checkpointLocation", "./check")\
    .trigger(processingTime='30 seconds').start()
query.awaitTermination()