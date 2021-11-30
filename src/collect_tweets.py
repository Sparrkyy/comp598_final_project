import tweepy
import datetime
import pandas as pd
import os
from dotenv import load_dotenv, find_dotenv

def get_tweets(api_client: tweepy.Client, search_query: str, start_day_shift: int, limit: int) -> pd.DataFrame:
    delta = datetime.timedelta(days=start_day_shift)

    start_time = datetime.datetime.utcnow() - delta
    df = pd.DataFrame(columns=['id', 'author_id', 'created_at', 'text'])
    count = 0

    for tweet in tweepy.Paginator(api_client.search_recent_tweets, query=search_query, max_results=100,
                                  start_time=start_time,
                                  tweet_fields=['created_at', 'author_id']).flatten(limit=limit):
        if tweet.id and tweet.author_id and tweet.created_at and tweet.author_id not in df['author_id']:
            count += 1
            df.loc[len(df)] = [tweet.id, tweet.author_id, tweet.created_at, tweet.text]

    if count < limit:
        for tweet in tweepy.Paginator(client.search_recent_tweets, query=query, max_results=100, start_time=start_time,
                                      end_time=df['created_at'].iloc[-1],
                                      tweet_fields=['created_at', 'author_id']).flatten(limit=limit - count):
            if tweet.id and tweet.author_id and tweet.created_at and tweet.author_id not in df['author_id']:
                count += 1
                df.loc[len(df)] = [tweet.id, tweet.author_id, tweet.created_at, tweet.text]

    df.set_index('id', inplace=True)
    return df


def write_to_csv(df: pd.DataFrame, output_file: str) -> None:
    df.to_csv(output_file)


if __name__ == '__main__':
    load_dotenv(find_dotenv())

    client = tweepy.Client(bearer_token= os.environ.get('TOKEN'))
    query = '(#ShangChi OR ShangChi OR #Shang-Chi OR Shang-Chi OR Shang_Chi) -is:retweet lang:en'

    df: pd.DataFrame = get_tweets(client, query, 3, 1000)

    write_to_csv(df, '../data/collection.csv')
