from TwitterSearch import *
import time
import datetime
from jinja2 import Template, Environment, FileSystemLoader
import os
import pdfkit
from slugify import slugify
from keys import *

data=[]
client = "Ford Smart Journey"
#keywords = ['multitouch.devpost.com', 'j.mp/1QMGD4k', 'Multi-Touch Multi-Hack']
keywords = ['#FordMxSmartJourney', 'j.mp/1T7uZCi', 'ford smart journey', 'fordsmartjourney.devpost.com']
#keywords = ['#IntelligentWorld','intelligentworld.devpost.com', 'j.mp/1SiGFrN']
#keywords = ['j.mp/22iwfJF', '#SparkBizApps', 'apachespark.devpost.com']


# jinja stuff
THIS_DIR = os.path.dirname(os.path.abspath(__file__))
def toHTML(data, client):

    fn = slugify(client + " "+ datetime.date.today().strftime('%m/%d/%y'))
    jenv = Environment(loader=FileSystemLoader(THIS_DIR), trim_blocks=True)
    tmpl = jenv.get_template('template.html')
    out = tmpl.render(data=data, client=client)
    with open(fn+'.html', "wb") as fh:
        fh.write(out.encode('utf-8'))
    pdfkit.from_string(out, fn+'.pdf')

try:
    ts = TwitterSearch(
          consumer_key = ck,
          consumer_secret = cs,
          access_token = at,
          access_token_secret = ast
       )
    tso = TwitterSearchOrder()
    tso.set_keywords(keywords, or_operator=True)
    for tweet in ts.search_tweets_iterable(tso):

        ts = time.strftime('%m-%d-%y %H:%M', time.strptime(tweet['created_at'],'%a %b %d %H:%M:%S +0000 %Y'))

        print( '[%s] @%s tweeted: %s, http://twitter.com/statuses/%s, RT: %s\n' % ( ts, tweet['user']['screen_name'], tweet['text'], tweet['id'], tweet['retweet_count']) )

        data.append({'date': ts, 'text': tweet['text'], 'avatar': tweet['user']['profile_image_url_https'], 'user': tweet['user']['screen_name'], 'id': tweet['id'], 'rt': tweet['retweet_count']})

    #print data
    toHTML(data, client)

except TwitterSearchException as e:
    print(e)
