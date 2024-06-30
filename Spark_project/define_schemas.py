# import required libraries
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, IntegerType, FloatType, StringType, StructField

# Build a spark session
spark = SparkSession.builder.appName("employees").getOrCreate()

# Define the schema 
# False' indicates null values are NOT allowed for the column.
schema = StructType([
    StructField("Emp_Id", StringType(), False),
    StructField("Emp_Name", StringType(), False),
    StructField("Department", StringType(), False),
    StructField("Salary", IntegerType(), False),
    StructField("Phone", StringType(), True),
])

#create a dataframe on top a csv file in spark
df = (spark.read
    .format("csv")
    .schema(schema)
    .option("header", "true")
    .load("employees.csv")
)
# display the dataframe content
df.show()

# Display the schema 
df.printSchema()

# Close the spark session
spark.stop()