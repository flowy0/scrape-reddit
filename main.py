import get_data_with_praw

if __name__ == "__main__":
    get_data_with_praw.get_data(topic="MachineLearning", limit=100, file_output="ml.csv")
