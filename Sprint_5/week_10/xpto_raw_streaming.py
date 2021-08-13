import tweepy
from tweepy import Stream
from tweepy.streaming import StreamListener
from smart_open import open
import json
from datetime import datetime

twitter_keys = {
    'consumer_key': 'xsLmIoXBMS5AyP9ApgjlVDutz',
    'consumer_secret': 'efjjVQrGOZfMQwNSZPXXAbEp0YpTBgvDUvzgwzy3dlJzcZqxMU',
    'access_token_key': '841044884048007170-QFO951QfYWjL4YjJVQ5oIV56b3BWKWy',
    'access_token_secret': '7VYCyHDZ79GfU1KcKrAG281ua453PWIG0yIBHw01GZx3l'
}


class TweetsListener(StreamListener):

    def __init__(self, file):
        self.file = file
        self.array = []

    def on_data(self, data):
        tweet = json.loads(data)
    
        try:
            formattedDate = datetime.strftime(datetime.strptime(tweet['created_at'], '%a %b %d %H:%M:%S %z %Y'), '%Y-%m-%d %H:%M:%S')
            
            if 'extended_tweet' in tweet.keys():
                strTweet = json.dumps({"id": tweet['id'],
                                       "text": tweet['extended_tweet']['full_text'],
                                       "created_at": formattedDate,
                                       "source": tweet['source'],
                                       "retweets": tweet['retweet_count']
                                      },
                                     indent=4, sort_keys=True)       
            elif 'text' in tweet.keys():
                strTweet = json.dumps({"id": tweet['id'],
                                       "text": tweet['text'],
                                       "created_at": formattedDate,
                                       "source": tweet['source'],
                                       "retweets": tweet['retweet_count']
                                      },
                                     indent=4, sort_keys=True)
  
            tweet_py = json.loads(strTweet)
            self.array.append(tweet_py)
            print(tweet_py)     

            if len(self.array) > 100:

                formatted_date_first_tweet = datetime.strftime(datetime.strptime(self.array[0]['created_at'],  '%Y-%m-%d %H:%M:%S'), '%Y%m%d_%H%M%S')
                
                with open(self.file + formatted_date_first_tweet + ".json", 'w') as f:
                    f.write(json.dumps(self.array, indent=4, sort_keys=True))
                    self.array = []

            return True

        except BaseException as e:
            print("Erro:", e)
        return False

    def on_error(self, status):
        print(status)

if __name__ == '__main__':

    search_words = ['Bolsonaro', 'Presidente do Brasil']
    auth = tweepy.OAuthHandler(twitter_keys['consumer_key'], twitter_keys['consumer_secret'])
    auth.set_access_token(twitter_keys['access_token_key'], twitter_keys['access_token_secret'])
    api = tweepy.API(auth)
    file = r'C:\Users\Rafael\Downloads\python\stream\twitter_'
    twitter_stream = Stream(auth = api.auth, listener=TweetsListener(file), lang='pt-br')
    twitter_stream.filter(track = search_words)

