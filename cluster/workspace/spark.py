import logging
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, desc, rank
from pyspark.sql.window import Window

# Configure logging
logging.getLogger("py4j").setLevel(logging.WARN)

# Initialize Spark Session
spark = SparkSession.builder \
    .appName("UberAnalysis") \
    .config("spark.ui.showConsoleProgress", "false") \
    .config("spark.log.level", "WARN") \
    .getOrCreate()

# Set log level
sc = spark.sparkContext
sc.setLogLevel("WARN")

# Read the Uber dataset
df = spark.read.csv("/opt/workspace/uber_data.csv", header=True, inferSchema=True)

# Group by base and date, then sum the trips
grouped_df = df.groupBy("dispatching_base_number", "date").sum("trips")

# Rename the aggregated column
grouped_df = grouped_df.withColumnRenamed("sum(trips)", "total_trips")

# Find the day with the most trips for each base
window_spec = Window.partitionBy("dispatching_base_number").orderBy(desc("total_trips"))
ranked_df = grouped_df.withColumn("rank", rank().over(window_spec)).filter(col("rank") == 1)

# Select relevant columns
result_df = ranked_df.select("dispatching_base_number", "date", "total_trips")

# Show the result
result_df.show()

# Save the result to a CSV file
result_df.write.csv("/opt/workspace/uber_analysis_result.csv", header=True)

# Stop the Spark session
spark.stop()