from pyspark.sql import SparkSession

# Initialize a SparkSession
spark = SparkSession.builder \
    .appName("HelloWorldSparkJob") \
    .getOrCreate()

# Print Hello, World! using Spark
print("Hello, World! from Apache Spark!")

# Use Spark to create a simple DataFrame
data = [("Hello", "World"), ("Spark", "Job")]
df = spark.createDataFrame(data, ["Word1", "Word2"])

# Show the DataFrame
df.show()

# Stop the Spark session
spark.stop()
