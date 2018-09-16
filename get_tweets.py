#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv
import json
import os
import sys

import config

#http://www.tweepy.org/
import tweepy

consumer_key = config.consumer_key
consumer_secret = config.consumer_secret
csv_ext = '.csv'
if (config.delimiter == '\t'):
    csv_ext = '.tsv'

def mkdir(path):
    if not os.path.exists(path):
        print "create directory: " + path 
        os.makedirs(path)

#method to get a user's last 100 tweets
def get_tweets(username):
    mkdir(username)
    #http://tweepy.readthedocs.org/en/v3.1.0/getting_started.html#api
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(config.access_token, config.access_token_secret)
    #api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())
    api = tweepy.API(auth)

    #set count to however many tweets you want; twitter only allows 200 at once
    number_of_tweets = 100

    #get tweets
    tweets = api.user_timeline(screen_name = username,count = number_of_tweets)


    #write to a new csv file from the array of tweets
    for tweet in tweets :
        tdir = os.path.join(username, str(tweet.created_at).split(' ')[0])
        print tweet.created_at
        mkdir(tdir)
        with open(os.path.join(tdir, "{0}.json".format(tweet.id_str)), 'w+') as ofile:
            ofile.write(json.dumps(tweet._json))
            ofile.close()


        with open(tdir + csv_ext, 'a') as csvfile:
            tweet_for_csv = [tweet.id_str, tweet.created_at, tweet.text.encode("utf-8")]
            writer = csv.writer(csvfile, delimiter=config.delimiter)
            writer.writerows([tweet_for_csv])
            csvfile.close()

#if we're running this as a script
if __name__ == '__main__':

    #get tweets for username passed at command line
    if len(sys.argv) == 2:
        alias = sys.argv[1]
        get_tweets(sys.argv[1])
    else:
        print "Error: enter one username"

    #alternative method: loop through multiple users
	# users = ['user1','user2']

	# for user in users:
	# 	get_tweets(user)
