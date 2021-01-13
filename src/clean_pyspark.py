# clean_data_pyspark.py



import pyspark.sql.functions as F
from pyspark.sql.types import IntegerType, StringType, TimestampType
import logging 
logger = logging.getLogger()

def change_types(df):
    logger.info("Updating Data Types")
    df = df.withColumn('score', F.col("score").cast(IntegerType()))
    # df = df.withColumn('created_utc', F.col("created_utc").cast(TimestampType()))

    df.printSchema()
    return df

def add_columns(df):
    logger.info("Add some date columns")
    df_new = (df.withColumn("timestamp", F.from_unixtime(df.created_utc, 'GMT')))
    # df = (df.select("created_utc").withColumn("dayofweek", dayofweek("created_utc")))
    logger.info(df_new.printSchema())
    # df_new.show(truncate=False)
    return df_new

def check_new_columns(df, col_name):
    logger.info(df.filter(F.col(col_name).isNotNull()).show())

def clean_data(df):
    df = change_types(df)
    df = add_columns(df)
    return df