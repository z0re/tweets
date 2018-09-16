#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv
import json
import os
import sys
import urllib
import get_tweets

def mkdir(path):
    if not os.path.exists(path):
        print "create directory: " + path 
        os.makedirs(path)

#if we're running this as a script
if __name__ == '__main__':

    #get tweets for username passed at command line
    if len(sys.argv) == 2:
        alias = sys.argv[1]
        max_id = '9040919820752101376'
        while True:
            max_id = get_tweets.get_tweets(sys.argv[1], max_id=max_id)
            print ("New max_id: " + max_id)
            if len(max_id) <= 0:
                break
            max_id = str(long(max_id) - 1)
    else:
        print "Error: enter one username"

