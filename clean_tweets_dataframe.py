from operator import index
import string
import pandas as pd
import numpy as np
from nltk.corpus import stopwords

class Clean_Tweets:
    """
    The PEP8 Standard AMAZING!!!
    """
    def __init__(self, df:pd.DataFrame):
        self.df = df
        print('Automation in Action...!!!')
        
    def drop_unwanted_column(self, df:pd.DataFrame)->pd.DataFrame:
        """
        remove rows that has column names. This error originated from
        the data collection stage.  
        """
        unwanted_rows = df[df['retweet_count'] == 'retweet_count' ].index
        df.drop(unwanted_rows , inplace=True)
        df = df[df['polarity'] != 'polarity']
        
        return df
    
    def drop_duplicate(self, df:pd.DataFrame)->pd.DataFrame:
        """
        drop duplicate rows
        """
        self.df.drop_duplicates(inplace=True)
        self.df.reset_index(drop=True, inplace=True)

        return self.df
 
    def convert_to_datetime(self, df:pd.DataFrame)->pd.DataFrame:
        """
        convert column to datetime
        """
        self.df['created_at'] = pd.to_datetime(
            self.df["created_at"], errors="coerce")
        
        return self.df

        df = df[df['created_at'] >= '2020-12-31' ]
        
        return df
    
    def convert_to_numbers(self, df:pd.DataFrame)->pd.DataFrame:
        """
        convert columns like polarity, subjectivity, retweet_count
        favorite_count etc to numbers
        """
        self.df[['polarity','subjectivity', 'retweet_count','favorite_count']]= self.df[['polarity','subjectivity',
        'retweet_count','favorite_count']].apply(pd.to_numeric, errors='coerce')
      

        return self.df
   
    def remove_non_english_tweets(self, df:pd.DataFrame)->pd.DataFrame:
        """
        remove non english tweets from lang
        """
        
        df = df.drop(self.df[self.df['lang']!= 'en'].index)
        
        return df
   
    def preprocessing_tweet(self, df:pd.DataFrame)->pd.DataFrame:
        """
        Preprocess the tweet full text 
        """
        #change to lower case
        self.df["full_text"] = self.df["full_text"].str.lower()

        #remove URL from full text
        self.df["full_text"] = self.df["full_text"].str.replace("http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+", " ")
        
        #remove Emojis
        self.df["full_text"] = self.df["full_text"].astype(str).apply(lambda x: x.encode('latin-1', 'ignore').decode('latin-1'))

        #remove symbols text 
        self.df["full_text"] = self.df["full_text"].str.replace('(\@w+.*?', " ")

        #remove punctatuation
        self.df["full_text"] = self.df["full_text"].apply(lambda x: " ".join([i for i in x if i not in string.punctuation]))

        #remove stop words from full text
        stopword_list = stopwords.words('english')
        self.df["full_text"] = self.df["full_text"].apply(lambda x: " ".join([w for w in x.split() if w not in (stopword_list)]))
 
        #drop empty tweets preprocessing
        self.df.drop(self.df[self.df["full_text"]== " "].index, inplace= True)

        return self.df

#add main function of class
if __name__ == "__main__":
    cleaned_df=pd.read_csv("data/processed_tweet_data.csv")
    Clean_Tweets = Clean_Tweets(cleaned_df)
    cleaned_df = Clean_Tweets.drop_duplicate(cleaned_df)
    cleaned_df = Clean_Tweets.remove_non_english_tweets(cleaned_df)
    cleaned_df = Clean_Tweets.convert_to_datetime(cleaned_df)
    cleaned_df = Clean_Tweets.drop_unwanted_column(cleaned_df)
    cleaned_df = Clean_Tweets.convert_to_numbers(cleaned_df)
    #print the first five row from cleaned tweet
    print(cleaned_df["polarity"].head())


    cleaned_df.to_csv("data/clean_processed_tweet.csv")
    print("Great File is successfully save!") 
