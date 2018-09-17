#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv
import json
import os
import sys
import urllib
import get_tweets

#if we're running this as a script
if __name__ == '__main__':

    #get tweets for username passed at command line
    if len(sys.argv) == 2:
        alias = sys.argv[1]
        max_id = '9040919820752101376'
        local_max_id = get_tweets.read_last_id(sys.argv[1])
        if len(local_max_id) > 0:
            max_id = local_max_id
            print ("Using local max_id: " + local_max_id)
        while True:
            max_id = get_tweets.get_tweets(sys.argv[1], max_id=max_id)
            print ("New max_id: " + max_id)
            if len(max_id) <= 0:
                break
            max_id = str(long(max_id) - 1)
    elif len(sys.argv) == 3:
        alias = sys.argv[1]
        action = sys.argv[2]
        if action == 'migrate_index':
            for fname in os.listdir(alias):
                if fname[-4:] == ".tsv":
                    tdir = os.path.join(alias, fname[:10])
                    src = os.path.join(alias, fname)
                    dst = os.path.join(tdir, "index"+fname[10:])
                    print (src, '->', dst)
                    os.rename(src,dst)
    else:
        print "Error: enter one username"

