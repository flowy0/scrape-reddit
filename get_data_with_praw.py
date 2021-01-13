# main.py

import pandas as pd
import praw
import datetime as dt
from dotenv import load_dotenv
import os
import pprint
import logging 
logger = logging.getLogger()


# get your secret variables from the .env file
def load_env():
    load_dotenv()
    return dict(os.environ)

def login(env_vars):
    reddit = praw.Reddit(client_id=env_vars['SCRIPT'], \
                        client_secret=env_vars['SECRET'], \
                        user_agent=env_vars['APP_NAME'], \
                        #  username=env_vars['REDDIT_USERNAME'], \
                        #  password=env_vars['REDDIT_PASSWORD']
                        )
    # to verify whether the instance is read-only instance or not 
    logger.info(f"Readonly instance: {reddit.read_only}") 

    return reddit


def print_attributes(input, topic):
    subreddit = input.subreddit(topic)

    sample_record = subreddit.hot(limit=1)
    # print 1 to look at the data formats
    for submission in sample_record:
        # check what attributes are available
        logger.info("Available attributes: \n")
        logger.info(pprint.pprint(vars(submission)))

        
def get_subreddit(input, topic, limit):
    # Assign a subreddit topic
    subreddit = input.subreddit(topic)

    top_subreddit = subreddit.hot(limit=limit)
    # create empty dict for appending
    topics_dict = { "title":[], \
                    "score":[], \
                    "url":[], \
                    "comms_num": [], \
                    "created_utc": [], \
                    "body":[]}

    for submission in top_subreddit:
        topics_dict["title"].append(submission.title)
        topics_dict["score"].append(submission.score)
        topics_dict["url"].append(submission.url)
        topics_dict["comms_num"].append(submission.num_comments)
        topics_dict["created_utc"].append(submission.created_utc)
        topics_dict["body"].append(submission.selftext)

    return topics_dict


def save_csv(input_dict, file_output):
    # save to csv
    topics_data = pd.DataFrame(input_dict)
    topics_data.to_csv(file_output, index=False)
    logger.info(f"saved data to {file_output}")
    logger.info(topics_data.info())


def get_data_as_dict(topic, limit):
    env_vars = load_env()
    reddit = login(env_vars)
    # print_attributes(input=reddit, topic=topic)
    data_dict = get_subreddit(input=reddit, topic=topic, limit=limit)
    return data_dict



if __name__ == "__main__":
    data_dict = get_data_as_dict(topic="Coffee", limit=100)
    save_csv(input_dict=data_dict, file_output="your_data.csv")


# selected_attr = ['created_utc', 'domain', 'title', 'selftext']
# reddit_comment = dict.fromkeys(selected_attr,[])
# {
    # "create":[], \
    # "num_comments": [], \
    # "body":[], \
    # "url": [], \
    # "created_utc:": [], \
    # }
# print(reddit_comment)

# for submission in selected_subreddit:
    # print(type(submission))
    # print(submission.selftext)
    # for attr, value in vars(submission).items():
        # if attr in selected_attr:
            # print(attr)
            # print(value)
            # reddit_comment[attr].append(value)
        # reddit_comment[attr].append(subreddit.title)

# print(reddit_comment)


# msg_df = pd.DataFrame(reddit_comment)
# print(msg_df)
# print(msg_df.info())

# msg_df.to_csv("sample_records.csv", index=False)

