import tweepy

from os import environ as env


consumer_key=env["CONSUMER_KEY"]
consumer_secret=env["CONSUMER_SECRET_KEY"]
access_token=env["TWITTER_ACCESS_TOKEN"]
access_token_secret=env["TWITTER_ACCESS_TOKEN_SECRET"]


consumer_key,consumer_secret,access_token,access_token_secret
auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)
                                 
api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("cool")
except:
    print("not so cool")

api.update_status(status = 'Hello World from Python')
# user = api.get_user(screen_name='SiriguppaNithin')
# id = user.id
# api.send_direct_message(id,"Hello")