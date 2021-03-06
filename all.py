from TwitterSearch import *
import time
import datetime
from jinja2 import Template, Environment, FileSystemLoader
import os
import pdfkit
from slugify import slugify
from keys import *

css = "pdf.css"
THIS_DIR = os.path.dirname(os.path.abspath(__file__))
def toHTML(data, client):

    fn = slugify(client + " "+ datetime.date.today().strftime('%m/%d/%y'))
    jenv = Environment(loader=FileSystemLoader(THIS_DIR), trim_blocks=True)
    tmpl = jenv.get_template('template.html')
    out = tmpl.render(data=data, client=client)
    with open('reports/'+fn+'.html', "wb") as fh:
        fh.write(out.encode('utf-8'))
    pdfkit.from_string(out, 'reports/'+fn+'.pdf', css=css)

q = {"Lenovo Multi-Touch Multi-Hack": ['multitouch.devpost.com', 'j.mp/1QMGD4k', 'Multi-Touch Multi-Hack'], "Ford Smart Journey": ['#FordMxSmartJourney', 'j.mp/1T7uZCi', 'ford smart journey', 'fordsmartjourney.devpost.com'], "GE Predix": ['#IntelligentWorld','intelligentworld.devpost.com', 'j.mp/1SiGFrN'], "Apache Spark Makers Build": ['j.mp/22iwfJF', '#SparkBizApps', 'apachespark.devpost.com'], "OpenShift Code Healthy": ['j.mp/202KkKz', '#CodeHealthy', 'openshift.devpost.com']}

for key in q:
  print "hackathon:", key
  print "search terms:", q[key]
  tweets=[]

  try:
      ts = TwitterSearch(
            consumer_key = ck,
            consumer_secret = cs,
            access_token = at,
            access_token_secret = ast
         )
      tso = TwitterSearchOrder()
      tso.set_keywords(q[key], or_operator=True)
      for tweet in ts.search_tweets_iterable(tso):

          ts = time.strftime('%m-%d-%y %H:%M', time.strptime(tweet['created_at'],'%a %b %d %H:%M:%S +0000 %Y'))

          #print( '[%s] @%s tweeted: %s, http://twitter.com/statuses/%s, RT: %s\n' % ( ts, tweet['user']['screen_name'], tweet['text'], tweet['id'], tweet['retweet_count']) )

          tweets.append({'date': ts, 'text': tweet['text'], 'avatar': tweet['user']['profile_image_url_https'], 'user': tweet['user']['screen_name'], 'id': tweet['id'], 'rt': tweet['retweet_count']})

      toHTML(tweets, key)

  except TwitterSearchException as e:
      print(e)
