# get_tweets.py
Python Script to Download Tweets

Use this script to download the last 100 (or whatever number you choose) from any Twitter user.

## Installation & How To Use

```
$ git clone https://github.com/liruqi/get_tweets.git
$ cd get_tweets
```
You may need to get your Twitter API Credentials by creating a new app at apps.twitter.com. Enter the appropriate API keys in config.py.

Then you can run the script by entering one username at the command line:

```
$ python get_all_tweets.py [twitter_username]
```

<br>or you can use interactive mode

```
$ python
>>> from get_tweets import get_tweets
>>> get_tweets("[twitter_username]")
```

## TODO
* Download images and video
* Export liked tweets
* Export lists
* Export to Excel

## More
http://www.getlaura.com/how-to-download-tweets-from-the-twitter-api/
