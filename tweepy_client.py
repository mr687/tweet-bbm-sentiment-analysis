import tweepy
import os

class TweepyClient:
	def __init__(self, config):
		self.config = config
		auth = tweepy.OAuth2AppHandler(
			consumer_key=config.get('consumerKey'),
			consumer_secret=config.get('consumerSecret'),
		)
		self.api = tweepy.API(auth=auth)

	def get_tweets(self, query):
		i = 1
		result = []
		for item in tweepy.Cursor(self.api.search_tweets, q=query, lang='id', result_type='mixed', count=1000, tweet_mode="extended").items():
			print(f'{i} processing...')
			if len(result) == 1000:
				break
			result.append([item.id, item.created_at.strftime("%d-%b-%Y (%H:%M:%S)"), item.full_text.replace("\n", " ")])
			i += 1
		return result
