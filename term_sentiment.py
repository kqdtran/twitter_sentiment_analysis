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

    # Evaluate the sentiment of every term by first evaluating the sentiment
    # of each tweet. The final sentiment score of a term is the sum of the
    # all the sentiments of the tweets it appears in divided by the number
    # of tweets it appears in
    all_term = {}
    for tweet in tweets:
        # First compute the sentiment of every tweet based on the words'
        # sentiment dictionary
        sentiment = 0.0
        for word in tweet.split(" "):
            if word in scores:
                sentiment += scores[word]

        # Assign the sentiment score computed above to every word in the tweet
        for word in tweet.split(" "):
            if word not in scores:
                if word not in all_term:
                    all_term[word] = [sentiment, 1] # a list of sentiment and count
                else: 
                    all_term[word][0] += sentiment
                    all_term[word][1] += 1

    final_sentiment = {term:all_term[term][0]/all_term[term][1] for term in all_term}
    for term in final_sentiment:
        print term, final_sentiment[term]

if __name__ == '__main__':
    main()
