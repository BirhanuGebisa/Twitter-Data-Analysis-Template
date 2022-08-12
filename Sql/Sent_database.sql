-- Active: 1660309191091@@127.0.0.1@3306@tweets
--""
--Create table if not exists
--contain table columns of twitter dataset
--""
CREATE TABLE IF NOT EXISTS Sentiment_Analysis_Table
(id INT NOT NULL AUTO_INCREMENT,
    created_at TEXT NOT NULL,
    full_text TEXT DEFAULT NULL,
    polarity FLOAT DEFAULT NULL,
    subjectivity FLOAT DEFAULT NULL,
    lang TEXT DEFAULT NULL,
    hashtags TEXT DEFAULT NULL,
    user_mentions TEXT DEFAULT NULL,
    place TEXT DEFAULT NULL,
    PRIMARY KEY (id)
)
ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE utf8mb4_unicode_ci