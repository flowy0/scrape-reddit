# main.py

import pandas as pd
import praw
import datetime as dt
from dotenv import load_dotenv
import os


# get your secret variables from the .env file
load_dotenv()
env_vars = dict(os.environ)


reddit = praw.Reddit(client_id=env_vars['SCRIPT'], \
                     client_secret=env_vars['SECRET'], \
                     user_agent=env_vars['APP_NAME'], \
                     username=env_vars['REDDIT_USERNAME'], \
                     password=env_vars['REDDIT_PASSWORD'])


# Assign a subreddit topic
subreddit = reddit.subreddit('Coffee')

# print the top 2 to look at the data formats
for submission in subreddit.hot(limit=2):
    print(submission.title)
