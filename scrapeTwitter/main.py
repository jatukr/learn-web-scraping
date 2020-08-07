from twitter_scraper import get_trends, get_tweets

print(get_trends())

getTweets = get_tweets('#malamjumat', pages=1)
for tweets in getTweets:
    print(tweets['text'])
