from textblob import TextBlob
import tweepy


cus_key=''
cus_secret= ''
acess_tok= ''
acess_tok_sec=''

auth= tweepy.OAuthHandler(cus_key,cus_secret)
auth.set_access_token(acess_tok,acess_tok_sec)

api= tweepy.API(auth)
#Count to measure tweets
#Search Keyword can be anything
tweet= api.search("Avengers: Infinity War",count=100)
#TO print tweets and viewing its sentiment
for tw in tweet:
    if tw.lang=="en":
        print(tw.text.encode("utf-8", errors='ignore'))
        analysis= TextBlob(tw.text)
        print(analysis.sentiment)
        print('\n')
