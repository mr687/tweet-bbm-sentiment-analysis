from dotenv import load_dotenv
from pathlib import Path
from tweepy_client import TweepyClient

import os
import csv

envPath = Path('.')/'.env'
load_dotenv(dotenv_path=envPath)

config = {
	"twitter": {
		"consumerKey": os.getenv('TWITTER_CONSUMER_KEY'),
		"consumerSecret": os.getenv('TWITTER_CONSUMER_SECRET'),
		"accessToken": os.getenv('TWITTER_ACCESS_TOKEN'),
		"accessTokenSecret": os.getenv('TWITTER_ACCESS_TOKEN_SECRET'),
		"bearerToken": os.getenv('TWITTER_BEARER_TOKEN'),
	}
}

def main():
	if __name__ == '__main__':
		client = TweepyClient(config.get('twitter'))
		
		q = 'riski bilar banting istri' # keyword
		tweets = client.get_tweets(q)
		
		with open(f"data.csv", "w", newline="\n", encoding="utf-8") as file:
			writer = csv.writer(file)
			writer.writerow(["id", "date", "tweet"])
			writer.writerows(tweets)

main()