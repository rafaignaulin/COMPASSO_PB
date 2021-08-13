import tweepy
from tweepy import Stream
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
import socket
import json

consumer_key='xsLmIoXBMS5AyP9ApgjlVDutz'
consumer_secret='efjjVQrGOZfMQwNSZPXXAbEp0YpTBgvDUvzgwzy3dlJzcZqxMU'
access_token ='841044884048007170-QFO951QfYWjL4YjJVQ5oIV56b3BWKWy'
access_secret='7VYCyHDZ79GfU1KcKrAG281ua453PWIG0yIBHw01GZx3l'

class TweetsListener(StreamListener):
  def __init__(self, csocket):
    self.client_socket = csocket

  def on_data(self, data):
    try:  
      msg = json.loads( data )
      print("Mensagem chegou")
      if "extended_tweet" in msg:
        self.client_socket\
            .send([msg['id'], msg['created_at'], str(msg['extended_tweet']['full_text'])]\
            ).encode('utf-8')         
        print(msg['extended_tweet']['full_text'])
     
      else:
        self.client_socket\
            .send([msg['id'], msg['created_at'], str(msg['text'])]\
            ).encode('utf-8')
        print(msg['text'])
      return True

    except BaseException as e:
        print("Erro: %s" % str(e))
    return True

  def on_error(self, status):
    print(status)
    return True

def sendData(c_socket, keyword):
  #auth
  auth = OAuthHandler(consumer_key, consumer_secret)
  auth.set_access_token(access_token, access_secret)

  twitter_stream = Stream(auth, TweetsListener(c_socket), lang='pt-br')
  twitter_stream.filter(track = keyword)

if __name__ == "__main__":
    s = socket.socket()
    host = "0.0.0.0"    
    port = 5555
    s.bind((host, port))
    s.listen(4)
    print('Socket iniciado')
    c_socket, addr = s.accept()
    print("Request de: " + str(addr))
    sendData(c_socket, keyword = ['Bolsonaro'])