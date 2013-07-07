from __future__ import division
import sys
import json

states = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA", 
          "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", 
          "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", 
          "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", 
          "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]

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

        # make sure that we're not getting invalid data
        if 'text' in data.keys() and 'place' in data.keys() and data['place'] != None:
            text = data['text'].replace("\n", "").encode('utf-8').strip()
            country = data['place']['country_code']
            state = data['place']['full_name'].encode('utf-8').strip()[-2::1]

            # now filter out US tweets with valid state codes
            if country == 'US' and state in states:
                tweets.append((text, state))

    # A sentiment of a tweet is simply the sum of the sentiment of every word
    # in the tweet that appears in the words' sentiment dictionary
    # Afterward, decides which state is happiest
    state_sentiment = {code:[0, 1] for code in states} # 1st is sum, 2nd is count
    for (tweet, state) in tweets:
        sentiment = 0.0
        for word in tweet.split():
            if word in scores:
                sentiment += scores[word]
        state_sentiment[state][0] += sentiment
        state_sentiment[state][1] += 1
    state_sentiment_final = {code:state_sentiment[code][0] / state_sentiment[code][1] for code in states}
    print sorted(state_sentiment_final, key = state_sentiment_final.get)[-1] # get the max
        

if __name__ == '__main__':
    main()
