import tweepy
from decouple import config

auth = tweepy.OAuthHandler(config('TWITTER_API_KEY'), config('TWITTER_API_SECRET'))
auth.set_access_token(config('TWITTER_ACCESS_TOKEN'), config('TWITTER_ACCESS_SECRET'))
api = tweepy.API(auth)

def get_popular_tweets(query="meme", count=10):
    tweets = api.search_tweets(q=query, result_type="popular", count=count)
    return [
        {
            "text": tweet.text,
            "user": tweet.user.screen_name,
            "retweets": tweet.retweet_count,
            "likes": tweet.favorite_count,
            "url": f"https://twitter.com/{tweet.user.screen_name}/status/{tweet.id}"
        }
        for tweet in tweets
    ]
