from __future__ import division
import sys
import json
import re

def main():
    tweet_file = open(sys.argv[1])

    # Build a list of tweets from the raw data
    tweets = []
    for line in tweet_file:
        data = json.loads(line)
        if 'text' in data.keys():
            tweets.append(data['text'].replace("\n", "").encode('utf-8'))
    tweets = filter(bool, tweets)

    # Evaluate the frequency of every term by the following formula
    # [# of occurrences of the term in all tweets] / [# of occurrences of all terms in all tweets]
    all_terms = {}
    total_terms = 0
    for tweet in tweets:
        terms_of_tweet = tweet.split()
        total_terms += len(terms_of_tweet)
        for word in terms_of_tweet:
            if word not in all_terms:
                all_terms[word] = 1.0 
            else: 
                all_terms[word] += 1.0

    for term in all_terms:
        print term, all_terms[term] / total_terms

if __name__ == '__main__':
    main()
