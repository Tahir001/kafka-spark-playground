# Do some basic ETL (Read, Analyze, Transform, and load the data)

# Import required libraries 
import pandas as pd
from pyspark.sql import SparkSession
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Create a spark session 

# At the start of your script
logger.info("Starting Spark session")
spark = SparkSession.builder.appName("cars").getOrCreate()

# Create a DF from pandas df
mtcars = pd.read_csv("mtcars.csv")

# Create a spark df from pandas df
sdf = spark.createDataFrame(mtcars) 

# View the schema
sdf.printSchema()

sdf.show(10)

# Show a specific column 
sdf.select('mpg').show(5)

# Filter a column
sdf_filtered = sdf.filter(sdf['mpg'] < 18)

# Aggregate some data -- Count the number of occurrences of each unique value in the cyl column
# groupby("cyl") groups the data by the cyl column.
# agg({"wt": "count"}) aggregates the data by counting the wt column.
# sort("count(wt)", ascending=False) sorts the aggregated results by the count of wt in descending order.
car_counts = sdf.groupby("cyl").agg({"wt": "count"}).sort("count(wt)", ascending=False).show(5)

# Output:
# +---+---------+
# |cyl|count(wt)|
# +---+---------+
# |  8|       14|
# |  4|       11|
# |  6|        7|
# +---+---------+

# Show the filtered DataFrame
sdf_filtered.show()

# Export the filtered DataFrame to a Parquet file
sdf_filtered.write.parquet("filtered_mtcars.parquet")

# Stop the Spark session
# Just before spark.stop()
logger.info("Spark session complete. Web UI should be available.")

input("Press Enter to terminate...")
# spark.stop()
