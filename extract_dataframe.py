import json
import pandas as pd
from textblob import TextBlob


def read_json(json_file: str)->list:
    """
    json file reader to open and read json files into a list
    Args:
    -----
    json_file: str - path of a json file
    
    Returns
    -------
    length of the json file and a list of json
    """
    
    tweets_data = []
    for tweets in open(json_file,'r'):
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

    # number of tweet count
    def find_statuses_count(self)->list:
        statuses_count = [x['user']['statuses_count'] for x in self.tweet_list]
        return statuses_count
     #full text of retweet   
    def find_full_text(self)->list:
        text = []
        for x in self.tweets_list:
            try:
                text.append(x['retweeted_status']['extended_tweet']['full_text'])
            except KeyError:
                text.append(x['text'])
        
        return text
    #find sentiments of text using TextBlob
    def find_sentiments(self, text)->list:

        polarity = [TextBlob(x).polarity for x in text]
        Subjectivity = [TextBlob(x).subjectivity for x in text]
        
        return polarity, self.subjectivity
    #created time of tweet
    def find_created_time(self)->list:
       created_at = [x["created_at"] for x in self.tweets_list]
       
       return created_at
    #source of tweet text
    def find_source(self)->list:
        source = [["source"] for x in self.tweets_list]

        return source
    #screen name of users
    def find_screen_name(self)->list:
        screen_name = [x["user"]["followers_count"] for x in self.tweets_list]

        return screen_name
     #followers of user count      
    def find_followers_count(self)->list:
        followers_count = [x["user"]["followers_count"] for x in self.tweets_list]

        return followers_count
    #friends number  
    def find_friends_count(self)->list:
        friends_count = [x["user"]["freinds_count"] for x in self.tweets_list]

        return friends_count
    #sensitive tweets   
    def is_sensitive(self)->list:
        try:
            is_sensitive = [x['possibly_sensitive'] for x in self.tweets_list]
        except KeyError:
            is_sensitive = None

        return is_sensitive
    #find favourite count
    def find_favourite_count(self)->list:
        favourite_count = [x.get("retweeted_status", {}).get("favourite_count", 0) for x in self.tweets_list]
        
        return favourite_count
    #retweet count
    def find_retweet_count(self)->list:
        retweet_count = []
        for tweet in self.tweets_list:
            if 'retweeted_status' in self.tweets_list:
                retweet_count.append(tweet["retweeted_count"])
            else:
                retweet_count.append(None)

        return retweet_count     
    #hashtags count
    def find_hashtags(self)->list:
        hashtags = []
        for tweethash in self.tweets_list:
            hashtags.append(", ".join([hashtag_item['text'] for hashtag_item in tweethash["entities"]["hashtags"]]))

        return hashtags
    #mention on tweets   
    def find_mentions(self)->list:
        mentions = []
        for tweethash in self.tweets_list:
            mentions.append(", ".join([mention["sreen_name"] for mention in tweethash["entities"]["user_mentions"]]))
        
        return mentions
    #location of tweet  
    def find_location(self)->list:
        try:
            location = self.tweets_list['user']['location']
        except TypeError:
            location = ''
        
        return location

          
    def get_tweet_df(self, save=False)->pd.DataFrame:
        """required column to be generated you should be creative and add more features"""
        
        columns = ['created_at', 'source', 'original_text','polarity','subjectivity', 'lang', 'favorite_count', 'retweet_count', 
            'original_author', 'followers_count','friends_count','possibly_sensitive', 'hashtags', 'user_mentions', 'place']
        
        created_at = self.find_created_time()
        source = self.find_source()
        text = self.find_full_text()
        polarity, subjectivity = self.find_sentiments(text)
        lang = self.find_lang()
        fav_count = self.find_favourite_count()
        retweet_count = self.find_retweet_count()
        screen_name = self.find_screen_name()
        follower_count = self.find_followers_count()
        friends_count = self.find_friends_count()
        sensitivity = self.is_sensitive()
        hashtags = self.find_hashtags()
        mentions = self.find_mentions()
        location = self.find_location()
        data = zip(created_at, source, text, polarity, subjectivity, lang, fav_count, retweet_count, screen_name, follower_count, friends_count, sensitivity, hashtags, mentions, location)
        df = pd.DataFrame(data=data, columns=columns)

        if save:
            df.to_csv('data/processed_tweet_data.csv', index=False)
            print('File Successfully Saved.!!!')
        
        return df

#main code      
if __name__ == "__main__":
    # required column to be generated you should be creative and add more features
    columns = ['created_at', 'source', 'original_text','clean_text', 'sentiment','polarity','subjectivity', 'lang', 'favorite_count', 'retweet_count', 
    'original_author', 'screen_count', 'followers_count','friends_count','possibly_sensitive', 'hashtags', 'user_mentions', 'place', 'place_coord_boundaries']
    _, tweet_list = read_json("data/global_twitter_data.json")
    tweet = TweetDfExtractor(tweet_list)
    tweet_df = tweet.get_tweet_df() 

    # use all defined functions to generate a dataframe with the specified columns above