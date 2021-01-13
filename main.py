import get_data_with_praw
import load_pyspark
import clean_pyspark
import os 
import sys
import logging 
import logging.handlers




if __name__ == "__main__":

    # this can also be set in an .env file 
    FILE_RAW = "ml_raw.parquet"
    FILE_CLEAN = "ml_clean.parquet"
    LOG_FILE ="main_log.log"
    TOPIC="MachineLearning"
    LIMIT=50


    LOG_FORMATTER=logging.Formatter("%(asctime)s — %(name)s — %(levelname)s — %(message)s")
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(LOG_FORMATTER)

    file_handler = logging.handlers.TimedRotatingFileHandler(LOG_FILE, when="midnight")
    file_handler.setFormatter(LOG_FORMATTER)
    
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)


    logger.info("Get Data from Reddit API PRAW Package")
    data_dict = get_data_with_praw.get_data_as_dict(topic=TOPIC, limit=LIMIT)
    #save to csv
    # print("Saving Output:")
    # get_data_with_praw.save_csv(input_dict=data_dict, file_output="ml.csv")
    
    # or use pyspark
    spark = load_pyspark.init_spark()
    df = load_pyspark.create_pyspark_df_from_dict(spark_session=spark, input_dict=data_dict)
    df.write.mode('overwrite').save(FILE_RAW)

    if os.path.exists(FILE_RAW):
        # read data from parquet file
        df = spark.read.parquet(FILE_RAW)

        #load from csv -- avoid calling APIs repeatedly
        # df = load_pyspark.create_pyspark_df_from_csv(spark_session=spark, input_file="ml.csv")

        # do more operations with pyspark
        df =clean_pyspark.clean_data(df)
        # save as parquet file - cleanup up data
        df.write.mode('overwrite').save(FILE_CLEAN)
    else:
        logger.info("file not saved, please check code to extract data")

    #stop spark session
    spark.stop()