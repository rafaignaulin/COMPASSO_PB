import tweepy
from tweepy import Stream
from tweepy.streaming import StreamListener
import socket
from pyspark import SparkContext
from pyspark.sql import SparkSession
from pyspark.sql import functions as f


twitter_keys = {
    'consumer_key': 'xsLmIoXBMS5AyP9ApgjlVDutz',
    'consumer_secret': 'efjjVQrGOZfMQwNSZPXXAbEp0YpTBgvDUvzgwzy3dlJzcZqxMU',
    'access_token_key': '841044884048007170-QFO951QfYWjL4YjJVQ5oIV56b3BWKWy',
    'access_token_secret': '7VYCyHDZ79GfU1KcKrAG281ua453PWIG0yIBHw01GZx3l'
}


class TweetsListener(StreamListener):
  # tweet object listens for the tweets
  def __init__(self, csocket):
    self.client_socket = csocket
  def on_status(self, tweet):

    print([tweet.id, str(tweet.text), tweet.created_at], tweet.created_at)
    self.client_socket\
    .send([tweet.id, str(tweet.text), tweet.created_at].encode('utf-8'))

  def on_error(self, status):
    print(status)
    return True


def sendData(c_socket):
  search_words = ['Bolsonaro', 'Presidente do Brasil']
  auth = tweepy.OAuthHandler(twitter_keys['consumer_key'], twitter_keys['consumer_secret'])
  auth.set_access_token(twitter_keys['access_token_key'], twitter_keys['access_token_secret'])
  api = tweepy.API(auth)

  twitter_stream = Stream(auth = api.auth, listener=TweetsListener(c_socket), lang='pt-br')
  twitter_stream.filter(track = search_words)


if __name__ == "__main__":
    # server local
    s = socket.socket()
    host = "0.0.0.0"    
    port = 25126
    s.bind((host, port))
    s.listen(4)

    c_socket, addr = s.accept()
    print("Request vindo do endereco: " + str(addr))

    sendData(c_socket)