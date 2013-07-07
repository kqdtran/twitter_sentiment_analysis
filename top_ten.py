from __future__ import division
import sys
import json
import re

def main():
    tweet_file = open(sys.argv[1])

    # Build a list of tweets from the raw data
    hashtags = []
    for line in tweet_file:
        data = json.loads(line)
        if "entities" in data.keys():
            for elem in data["entities"]["hashtags"]:
                tag = elem["text"]
                hashtags.append(tag.replace("\n", "").encode('utf-8').strip())    

    # Evaluate the frequency of the hashtag and print out the top 10
    count_tags = {}
    for tag in hashtags:
        if tag in count_tags:
            count_tags[tag] += 1.0
        else:
            count_tags[tag] = 1.0
    top_ten = sorted(count_tags, key = count_tags.get)[-10::1]
    for tag in top_ten[::-1]:
        print tag, count_tags[tag]

if __name__ == '__main__':
    main()
