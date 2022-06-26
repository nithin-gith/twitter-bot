from json import load
import tweepy
import time

import os 
from dotenv import load_dotenv
load_dotenv()


from textblob import TextBlob as tb


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

my_id = int(api.get_user(screen_name="bot_jff").id_str)
mention_id=1

FILE_NAME = "last_id.txt"


def get_last_id(FILE_NAME):
    file_read = open(FILE_NAME,'r')
    mention_id = int(file_read.read().strip())
    file_read.close()
    return mention_id

def set_last_id(FILE_NAME,mention_id):
    file_write=open(FILE_NAME,'w')
    file_write.write(str(mention_id))
    file_write.close()
    return

while True:
    mentions = api.mentions_timeline(since_id=mention_id)
    for mention in mentions:
        mention_text = mention.text
        print(mention_text)   
        text_analysis = tb(mention_text)
        analysis_polarity = text_analysis.sentiment.polarity
        print(analysis_polarity)
        if mention.in_reply_to_status_id is None and mention.author.id != my_id:
            if analysis_polarity>=0:
                if analysis_polarity<0.3:
                    try:
                        api.create_favorite(id=mention.id)
                    except Exception as err:
                        print(err)
                else:
                    try:
                        api.create_favorite(id=mention.id)
                        api.retweet(id=mention.id)
                        print(mention.id)
                        api.update_status(status="Hi "+mention.author.name+", Thank you so much for your wonderful words ;)",in_reply_to_status_id=mention.id,auto_populate_reply_metadata=True)
                    except Exception as err:
                        print(err)
            else:
                try:
                    api.update_status(status="Hi "+mention.author.name+", So sad to hear that from you :( Please check your DM and give us the feedback for improvement",in_reply_to_status_id=mention.id,auto_populate_reply_metadata=True)
                    api.send_direct_message(recipient_id=mention.author.id,text="Hi "+mention.author.name+", Please fill the below attached feedback form and help us improve :)")
                except Exception as err:
                    print(err)
        mention_id = mention.id
    time.sleep(5)




### positive
## <0.3 
# like 

## >0.3
# retweet
# like
# appreciate tweet

## negative
# send dm 
# apology reply
