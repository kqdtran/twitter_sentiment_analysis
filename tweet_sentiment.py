import sys
import json

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    
    # Build a dictionary of words' sentiment
    scores = {}
    for line in sent_file:
        term, score = line.split("\t") # tab-delimited
        scores[term] = int(score)

    # Build a list of tweets from the raw data
    tweets = []
    for line in tweet_file:
        data = json.loads(line)
        if 'text' in data.keys():
            tweets.append(data['text'].encode('utf-8'))

    # Evaluate the sentiment of a tweet based on the dictionary
    # A sentiment of a tweet is simply the sum of the sentiment of every word
    # in the tweet that appears in the words' sentiment dictionary
    for tweet in tweets:
        sentiment = 0.0
        for word in tweet.split(" "):
            if word in scores:
                sentiment += scores[word]
        print sentiment

if __name__ == '__main__':
    main()
