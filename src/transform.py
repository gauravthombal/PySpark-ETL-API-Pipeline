from pyspark.sql import SparkSession
from pyspark.sql.functions import explode

spark = SparkSession.builder \
    .appName("ETL Pipeline") \
    .getOrCreate()

# Read raw JSON
df = spark.read.json("data/raw/products.json")

# Flatten JSON
df = df.select(explode("products").alias("product"))

# Expand nested fields
df = df.select("product.*")

# Your transformations
df = df.dropDuplicates()
df = df.na.fill("Unknown")

# Save cleaned CSV
df.write.mode("overwrite").csv(
    "data/processed/products",
    header=True
)

# Save Parquet
df.write.mode("overwrite").parquet(
    "data/parquet/products"
)

spark.stop()