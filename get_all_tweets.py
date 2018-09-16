#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv
import json
import os
import sys
import urllib
import get_tweets

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

#if we're running this as a script
if __name__ == '__main__':

    #get tweets for username passed at command line
    if len(sys.argv) == 2:
        alias = sys.argv[1]
        max_id = ''
        while True:
            max_id = get_tweets.get_tweets(sys.argv[1])
            print ("New max_id: " + max_id)
            if len(max_id) <= 0:
                break
    else:
        print "Error: enter one username"

    #alternative method: loop through multiple users
	# users = ['user1','user2']

	# for user in users:
	# 	get_tweets(user)
