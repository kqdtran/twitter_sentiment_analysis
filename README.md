Based on Coursera's [Introduction to Data Science](https://class.coursera.org/datasci-001/class/index) Project 1

## About twitterstream.py: 

Used to fetch live stream data from twitter.

Requires oauth2, which is not part of the EnThought Python library.

## Usage
Open the program and replace access_token_key, access_token_secret, consumer_key, and consumer_secret with the appropriate values. Then run   

```python
python twitterstream.py 
```

To get credentials:

* Create a twitter account if you do not already have one.
* Go to [https://dev.twitter.com/apps](https://dev.twitter.com/apps) and log in with your twitter credentials.
* Click "create an application"
* Fill out the form and agree to the terms.  Put in a dummy website if you don't have one you want to use.
* On the next page, scroll down and click "Create my access token"
* Copy your "Consumer key" and your "Consumer secret" into twitterstream.py
* Click "Create my access token."  You can [read more about Oauth authorization](https://dev.twitter.com/docs/auth).
* Open twitterstream.py and set the variables corresponding to the consumer key, consumer secret, access token, and access secret     

> access_token_key = "<Enter your access token key here>"    
access_token_secret = "<Enter your access token secret here>"
 
> consumer_key = "<Enter consumer key>"     
consumer_secret = "<Enter consumer secret>"    

* Run the following and make sure you see data flowing.  

```python
python twitterstream.py    
```

To get sufficient data and run any of the py files, pipe the output into a text file, like  

```python
python twitterstream.py > output.txt     
```

, and make sure that you let it run for **at least** 10-15 minutes.

## Included examples    

	$ python tweet_sentiment.py <sentiment_file> <tweet_file>    
to print to stdout the sentiment of each tweet you retrieve in your tweet_file. The sentiment_file is AFINN-111.txt

	$ python term_sentiment.py <sentiment_file> <tweet_file>    
to derive the sentiment for new terms that wasn't provided in the sentiment file    

	$ python frequency.py <tweet_file>    
to compute term's frequency

	$ python happiest_state.py <sentiment_file> <tweet_file>    
to determine the happiest state, based on the number of tweets collected in tweet_file    

	$ python top_ten.py <tweet_file>    
to find the top ten hash tags in the number of tweets collected   

