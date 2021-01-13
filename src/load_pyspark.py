# pyspark_df

from pyspark.sql import SparkSession
import logging
logger = logging.getLogger()

def init_spark():
    spark = SparkSession.builder.appName("dataload").getOrCreate()
    logger.info(f"Spark Instance: {spark}")
    rdd = spark.sparkContext.parallelize([1,2,3,4])
    logger.info(f"RDD count: {rdd.count()}")
    return spark


def create_pyspark_df_from_dict(spark_session,input_dict):
    logger.info("Load the data from the dictionary")
    column_names, data = zip(*input_dict.items())
    df = spark_session.createDataFrame(zip(*data), column_names)
    logger.info(f"Data Type: {type(df)}")
    logger.info(f"Row Count of pyspark df :{df.count()}")
    logger.info(df.show())

    return df 

def create_pyspark_df_from_csv(spark_session,input_file):
    logger.info("Load the data from the input file")
    df = spark_session.read.csv(input_file, header=True, inferSchema=True)
    logger.info(f"Data Type: {type(df)}")
    logger.info(df.printSchema())
    logger.info(f"Row Count of pyspark df :{df.count()}")
    logger.info(df.show())

    return df 