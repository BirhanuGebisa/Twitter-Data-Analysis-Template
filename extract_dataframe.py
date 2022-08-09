import json
import pandas as pd
from textblob import TextBlob
from zipfile import ZipFile

#read the json file 
def read_json(json_file: str)->list:
    tweets_data = []
    for tweets in open("data/global_twitter_data.json",'r'):
        tweets_data.append(json.loads(tweets))
    
    
    return len(tweets_data), tweets_data

class TweetDfExtractor:
    """
    this function will parse tweets json into a pandas dataframe
    
    Return
    ------
    dataframe
    """
    def __init__(self, tweets_list):
        
        self.tweets_list = tweets_list
  
    def find_full_text(self)->list:
        text = []
        for x in self.tweets_list:
            try:
                text.append(x['retweeted_status']['extended_tweet']['full_text'])
            except KeyError:
                text.append(x['full_text'])
        
        return text
    #find sentiments of text using TextBlob
    def find_sentiments(self, full_text)->list:

        polarity = [TextBlob(x).polarity for x in full_text]
        subjectivity = [TextBlob(x).subjectivity for x in full_text]
        
        return polarity, subjectivity
    #created time of tweet
    def find_created_time(self)->list:
       created_at = [x["created_at"] for x in self.tweets_list]
       
       return created_at
    #source of tweet text
    def find_source(self)->list:
        source = [["source"] for x in self.tweets_list]

        return source
    #find favourite count
    def find_favourite_count(self)->list:
        favourite_count = [x.get("retweeted_status", {}).get("favourite_count", 0) for x in self.tweets_list]
        
        return favourite_count
    #retweet count
    def find_retweet_count(self)->list:
        retweet_count = []
        for tweet in self.tweets_list:
            if 'retweeted_status' in self.tweets_list:
                retweet_count.append(tweet["retweet_count"])
            else:
                retweet_count.append(None)

        return retweet_count     
    
    def find_lang(self)->list:
        lang = [x['lang'] for x in self.tweets_list]

        return lang
          
    def get_tweet_df(self, save=False)->pd.DataFrame:
        """required column to be generated you should be creative and add more features"""
        
        columns = ['created_at', 'source', 'full_text','polarity','subjectivity', 'lang', 'favorite_count', 'retweet_count']
        
        created_at = self.find_created_time()
        source = self.find_source()
        full_text = self.find_full_text()
        polarity, subjectivity = self.find_sentiments(full_text)
        lang = self.find_lang()
        fav_count = self.find_favourite_count()
        retweet_count = self.find_retweet_count()
        #possibly_sensitive  = self.is_sensitive()
        data = zip(created_at, source, full_text, polarity, subjectivity, lang, fav_count, retweet_count)
        df = pd.DataFrame(data=data, columns=columns)

        if save:
            df.to_csv('data/processed_tweet_data.csv', index=False)
            print('File Successfully Saved.!!!')
        
        return df

#main code      
if __name__ == "__main__":
    # required column to be generated you should be creative and add more features
    columns = ['created_at', 'source', 'full_text','clean_text', 'sentiment','polarity','subjectivity', 'lang', 'favorite_count', 'retweet_count','possibly_sensitive']
    _, tweet_list = read_json("data/global_twitter_data.json")
    tweet = TweetDfExtractor(tweet_list)
    tweet_df = tweet.get_tweet_df(save=True) 

    # use all defined functions to generate a dataframe with the specified columns above