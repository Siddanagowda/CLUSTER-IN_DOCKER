from pyspark.sql import SparkSession
from pyspark import SparkContext, SparkConf

# Initialize Spark session
conf = SparkConf().setAppName("UberDataAnalysis")
sc = SparkContext(conf=conf)
spark = SparkSession(sc)

# Set log level
sc.setLogLevel("WARN")

# Read the Uber dataset
df = spark.read.csv("/opt/workspace/uber_data.csv", header=True, inferSchema=True)

# Convert DataFrame to RDD
rdd = df.rdd

# Map phase: Create key-value pairs ((base, date), trips)
mapped_rdd = rdd.map(lambda row: ((row['dispatching_base_number'], row['date']), row['trips']))

# Reduce phase: Sum trips for each (base, date)
reduced_rdd = mapped_rdd.reduceByKey(lambda a, b: a + b)

# Map phase: Create key-value pairs (base, (date, total_trips))
base_date_rdd = reduced_rdd.map(lambda x: (x[0][0], (x[0][1], x[1])))

# Reduce phase: Find the day with the most trips for each base
max_trips_rdd = base_date_rdd.reduceByKey(lambda a, b: a if a[1] > b[1] else b)

# Collect the results
result = max_trips_rdd.collect()

# Convert result to DataFrame for better visualization
result_df = spark.createDataFrame(result, ["dispatching_base_number", "date_total_trips"])
result_df = result_df.select("dispatching_base_number", result_df["date_total_trips"].getField("_1").alias("date"), result_df["date_total_trips"].getField("_2").alias("total_trips"))

# Results
result_df.show()

# Write the result to a CSV file
result_df.write.csv("/opt/workspace/uber_analysis_result.csv", header=True)

# Stop the Spark context
sc.stop()