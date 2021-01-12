# pyspark_df

from pyspark.sql import SparkSession

def init_spark():
    spark = SparkSession.builder.appName("dataload").getOrCreate()
    print(f"Spark Instance: {spark}")
    rdd = spark.sparkContext.parallelize([1,2,3,4])
    print(f"RDD count: {rdd.count()}")
    return spark


def create_pyspark_df_from_dict(spark_session,input_dict):
    print("Load the data from the dictionary")
    column_names, data = zip(*input_dict.items())
    df = spark_session.createDataFrame(zip(*data), column_names)
    print(f"Data Type: {type(df)}")
    print(f"Row Count of pyspark df :{df.count()}")
    df.show()

    return df 

def create_pyspark_df_from_csv(spark_session,input_file):
    print("Load the data from the input file")
    df = spark_session.read.csv(input_file, header=True, inferSchema=True)
    print(f"Data Type: {type(df)}")
    print(df.printSchema())
    print(f"Row Count of pyspark df :{df.count()}")
    df.show()

    return df 