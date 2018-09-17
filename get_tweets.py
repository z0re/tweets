#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv
import json
import os
import sys
import urllib
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

def read_last_id(username):
    mipath = os.path.join(username, "max_id.txt")
    with open(mipath, 'r') as ofile:
        return ofile.read()
    return ""
 
def write_last_id(username, id_str):
    mipath = os.path.join(username, "max_id.txt")
    with open(mipath, 'w+') as ofile:
        ofile.write(id_str)
     
#method to get a user's last 100 tweets
def get_tweets(username, max_id = '1040919820752101376'):
    mkdir(username)
    #http://tweepy.readthedocs.org/en/v3.1.0/getting_started.html#api
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(config.access_token, config.access_token_secret)
    #api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())
    api = tweepy.API(auth)

    #set count to however many tweets you want; twitter only allows 200 at once
    number_of_tweets = 100

    #get tweets
    tweets = api.user_timeline(screen_name = username,count = number_of_tweets, max_id=max_id)
    print('max_id: ', max_id, len(tweets))

    #write to a new csv file from the array of tweets
    last_id = ""
    for tweet in tweets :
        tdir = os.path.join(username, str(tweet.created_at).split(' ')[0])
        print tweet.created_at
        mkdir(tdir)
        last_id = tweet.id_str
        writes = 0
        with open(os.path.join(tdir, "{0}.json".format(tweet.id_str)), 'w+') as ofile:
            ofile.write(json.dumps(tweet._json))
            ofile.close()
            writes += 1

        with open(os.path.join(tdir, "index" + csv_ext), 'a') as csvfile:
            tweet_for_csv = [tweet.user.screen_name, tweet.id_str, tweet.created_at, tweet.text.encode("utf-8")]
            writer = csv.writer(csvfile, delimiter=config.delimiter)
            writer.writerows([tweet_for_csv])
            csvfile.close()
            writes += 1

        with open(os.path.join(tdir, "index_urlencode" + csv_ext), 'a') as csvfile:
            tweet_for_csv = [tweet.user.screen_name, tweet.id_str, tweet.created_at, urllib.quote_plus(tweet.text.encode("utf-8"))]
            writer = csv.writer(csvfile, delimiter=config.delimiter)
            writer.writerows([tweet_for_csv])
            csvfile.close()
            writes += 1

        if writes == 3 and config.delete:
            if long(tweet.id_str) <  long(config.delete_max_id):
                print ("Delete tweet: " + tweet.id_str)
                api.destroy_status(tweet.id_str)
                config.delete_max_count -= 1
                if 0 >= config.delete_max_count:
                    write_last_id(username, tweet.id_str)
                    print ("Delete tweet: reached the maximum deletion count, exit.")
                    exit(1)
    write_last_id(username, last_id)
    return last_id

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
