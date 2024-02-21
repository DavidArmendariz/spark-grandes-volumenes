from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Hello World").getOrCreate()

print("Hello, World!")

spark.stop()
