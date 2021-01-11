# main.py

import pandas as pd
import praw
import datetime as dt
from dotenv import load_dotenv
import os
import pprint


# get your secret variables from the .env file
load_dotenv()
env_vars = dict(os.environ)


reddit = praw.Reddit(client_id=env_vars['SCRIPT'], \
                     client_secret=env_vars['SECRET'], \
                     user_agent=env_vars['APP_NAME'], \
                    #  username=env_vars['REDDIT_USERNAME'], \
                    #  password=env_vars['REDDIT_PASSWORD']
                     )
# to verify whether the instance is read-only instance or not 
print(f"Readonly instance: {reddit.read_only}") 

# Assign a subreddit topic
subreddit = reddit.subreddit('Coffee')

selected_subreddit = subreddit.hot(limit=1)

# print the top 2 to look at the data formats
# for submission in selected_subreddit:
    #check what attributes are available
    # pprint.pprint(vars(submission))

top_subreddit = subreddit.hot(limit=20)
topics_dict = { "title":[], \
                "score":[], \
                # "id":[], \
                "url":[], \
                "comms_num": [], \
                "created": [], \
                "body":[]}

for submission in top_subreddit:
    topics_dict["title"].append(submission.title)
    topics_dict["score"].append(submission.score)
    # topics_dict["id"].append(submission.id)
    topics_dict["url"].append(submission.url)
    topics_dict["comms_num"].append(submission.num_comments)
    topics_dict["created"].append(submission.created)
    topics_dict["body"].append(submission.selftext)

topics_data = pd.DataFrame(topics_dict)
file_output ='coffee_data.csv'
topics_data.to_csv(file_output, index=False)
print(f"saved data to {file_output}")


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

