from json import load
import tweepy
import time

import os 
from dotenv import load_dotenv
load_dotenv()

print(os.getenv("CONSUMER_KEY"))


consumer_key=os.getenv("CONSUMER_KEY")
consumer_secret=os.getenv("CONSUMER_SECRET_KEY")
access_token=os.getenv("TWITTER_ACCESS_TOKEN")
access_token_secret=os.getenv("TWITTER_ACCESS_TOKEN_SECRET")


auth = tweepy.OAuthHandler(consumer_key,consumer_secret,access_token,access_token_secret)
                                 
api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("cool")
except:
    print("not so cool")

my_id = api.get_user(screen_name="SiriguppaNithin").id
mention_id=1
reply = "Please check your DM"
message = "Hello, How may I help You :)"

# api.send_direct_message(my_id, "Hi Bro from python")

mentions = api.mentions_timeline(count=1)
while True:
    for mention in mentions:
        print(mention.text)
    time.sleep(5)

# if api.destroy_friendship(id=api.get_user(screen_name="Sreya_TV").id):
#     print ("Followed")
# else:
#     print ("Not Followed")

# tweets = api.user_timeline(id=my_id)
# for tweet in tweets:
#     print(str(tweet.id)+'-'+tweet.text)





# while 1 :
#     mentions=api.mentions_timeline(since_id=mention_id)
#     for mention in mentions:
#         if mention.created_at.timestamp()<time.time():
#             continue
#         print("Mention tweet found!")
#         mention_id = mention.id
#         if mention.author.id != my_id and mention.in_reply_to_status_id is None:
#             api.send_direct_message(mention.author.id,message)
#             try:
#                 api.update_status(reply,in_reply_to_mention_status_id=mention.id_str)
#                 print("replying")
#             except:
#                 print("failed")



# while 1:
#     mentions = api.mentions_timeline()
#     for mention in mentions:
#         print(mention.author.id)

