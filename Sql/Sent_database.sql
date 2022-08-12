CREATE TABLE IF NOT EXISTS 'SentimentTable'
('id'INT NOT NULL AUTO_INCREMENT,
    'created_at' TEXT NOT NULL,
    'source' VARCHAR(200) NOT NULL,
    'Original_Text' TEXT DEFAULT NULL,
    'full_text' TEXT DEFAULT NULL,
    'polarity' FLOAT DEFAULT NULL,
    'sentiment' FLOAT DEFAULT NULL,
    'lang' TEXT DEFAULT NULL,
    'favorite_count' INT DEFAULT NULL,
    'retweet_count' INT DEFAULT NULL,
    'possibly_sensitive' TEXT DEFAULT NULL, 
    'friends_count' INT DEFAULT NULL,
    'hashtags' TEXT DEFAULT NULL,
    'user_mentions' TEXT DEFAULT NULL,
    'place' TEXT DEFAULT NULL,
    PRIMARY KEY ('id')
)
ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE utf8mb4_unicode_ci;