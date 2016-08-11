from TwitterSearch import *
import time
import string
from datetime import datetime
from jinja2 import Template, Environment, FileSystemLoader
from os import environ

from flask import request, session, Flask, render_template, Response, redirect, url_for
from flask_cors import CORS, cross_origin

from sqlalchemy import *
from sqlalchemy.exc import IntegrityError
from sqlalchemy.exc import CompileError

# Initialise the Flask app ##
application = Flask(__name__)
application.config['PROPAGATE_EXCEPTIONS'] = True

@application.route('/', defaults={'path': ''})
@application.route('/<path:path>')
def main(path=None):
    if (path==''):
        return render_template('index.html')
    else:
        client = getClient(path)
        keywords = getKeywords(client)
        data = getTweets(keywords)
        return render_template('report.html', client=client, data=data)

def getTweets(keywords):
    data=[]
    try:
        ts = TwitterSearch(
              consumer_key = environ['CK'],
              consumer_secret = environ['CS'],
              access_token = environ['AT'],
              access_token_secret = environ['ATS']
           )
        tso = TwitterSearchOrder()
        tso.set_keywords(keywords, or_operator=True)
        for tweet in ts.search_tweets_iterable(tso):

            ts = time.strftime('%m-%d-%y %H:%M', time.strptime(tweet['created_at'],'%a %b %d %H:%M:%S +0000 %Y'))

            # print( '[%s] @%s tweeted: %s, http://twitter.com/statuses/%s, RT: %s\n' % ( ts, tweet['user']['screen_name'], tweet['text'], tweet['id'], tweet['retweet_count']) )

            data.append({'date': ts, 'text': tweet['text'], 'avatar': tweet['user']['profile_image_url_https'], 'user': tweet['user']['screen_name'], 'id': tweet['id'], 'rt': tweet['retweet_count']})

        return(data)

    except TwitterSearchException as e:
        print(e)

def getKeywords(client):
    keywords = ['#FordMxSmartJourney', 'j.mp/1T7uZCi', 'ford smart journey', 'fordsmartjourney.devpost.com']
    ## this should be a db call (nosql?)
    return keywords

def getClient(path):
    client = 'Ford Smart Journey'
    ## this should be a db call (nosql?)
    return client
