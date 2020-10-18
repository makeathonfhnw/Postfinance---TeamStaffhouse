# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.6.0
#   kernel_info:
#     name: python3-azureml
#   kernelspec:
#     display_name: Python 3.6 - AzureML
#     language: python
#     name: python3-azureml
# ---

# +
# Import the Twython class
from twython import Twython
import json
import pandas as pd

# Load credentials from json file
#with open("twitter_credentials.json", "r") as file:
#    creds = json.load(file)

# Instantiate an object
# Twitter API Keys would be available offline
python_tweets = Twython(['API Twitter Key'], ['API Twitter Secret Key'])

# Create our query
query = {'q': 'vulnerability tomcat',       
        'count': 10,
        'lang': 'en',
        }

# Search tweets
dict_ = {'user': [], 'date': [], 'text': [], 'favorite_count': []}
for status in python_tweets.search(**query)['statuses']:
    dict_['user'].append(status['user']['screen_name'])
    dict_['date'].append(status['created_at'])
    dict_['text'].append(status['text'])
    dict_['favorite_count'].append(status['favorite_count'])

# Structure data in a pandas DataFrame for easier manipulation
df = pd.DataFrame(dict_)
df.sort_values(by='favorite_count', inplace=True, ascending=False)
df.head(5)
# -



pip install python-Levenshtein

>>> a, b = 'spam and eggs', 'foo and bar'
>>> e = opcodes(a, b)
>>> apply_edit(inverse(e), b, a)
'spam and eggs'
>>> e[4] = ('equal', 10, 13, 8, 11)
>>> a, b, e
>>> apply_edit(e, a, b)
'foo and ggs'

pip install Twython
