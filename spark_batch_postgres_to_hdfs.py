from pyspark.sql import SparkSession
from pyspark.sql.functions import current_date

spark = SparkSession.builder \
    .appName("RandomUserBatchArchive") \
    .getOrCreate()

spark.sparkContext.setLogLevel("WARN")

# Read data from PostgreSQL
df = spark.read \
    .format("jdbc") \
    .option("url", "jdbc:postgresql://localhost:5432/randomuser_db") \
    .option("dbtable", "users") \
    .option("user", "postgres") \
    .option("password", "post") \
    .option("driver", "org.postgresql.Driver") \
    .load()

# Add partition column
df_with_date = df.withColumn("load_date", current_date())

# Write as Parquet partitioned by date to HDFS
df_with_date.write \
    .mode("append") \
    .partitionBy("load_date") \
    .parquet("/archive/randomuser/parquet")

spark.stop()
