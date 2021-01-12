import get_data_with_praw
import load_pyspark
import clean_pyspark

if __name__ == "__main__":
    # print("Get Data from Reddit API PRAW Package")
    # data_dict = get_data_with_praw.get_data_as_dict(topic="MachineLearning", limit=50)
    #save to csv
    # print("Saving Output:")
    # get_data_with_praw.save_csv(input_dict=data_dict, file_output="ml.csv")
    
    # or use pyspark
    spark = load_pyspark.init_spark()
    # df = load_pyspark.create_pyspark_df_from_dict(spark_session=spark, input_dict=data_dict)

    #load from csv -- avoid calling APIs repeatedly
    df = load_pyspark.create_pyspark_df_from_csv(spark_session=spark, input_file="ml.csv")

    # do more operations with pyspark
    df =clean_pyspark.change_types(df)
    df = clean_pyspark.add_columns(df)
    clean_pyspark.check_new_columns(df, "created_utc")