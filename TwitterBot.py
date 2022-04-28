import tweepy
import time

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

my_id = api.get_user(screen_name="bot_jff").id
mention_id=1
reply = "Please check your DM"
message = "Hello, How may I help You :)"


while 1 :
    mentions=api.mentions_timeline(since_id=mention_id)
    for mention in mentions:
        if mention.created_at.timestamp()<time.time():
            continue
        print("Mention tweet found!")
        mention_id = mention.id
        if mention.author.id != my_id and mention.in_reply_to_status_id is None:
            api.send_direct_message(mention.author.id,message)
            try:
                api.update_status(reply,in_reply_to_mention_status_id=mention.id_str)
                print("replying")
            except:
                print("failed")
# while 1:
#     mentions = api.mentions_timeline()
#     for mention in mentions:
#         print(mention.author.id)

