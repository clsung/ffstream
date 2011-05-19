import os
import oauth2 as oauth
import urllib
import urllib2
from urllib2 import HTTPError

def callAPI(path, **kw):
    api_url= lambda x: 'http://www.plurk.com/API%s' % x
    if 'api_key' not in kw.keys(): kw['api_key'] = os.environ["PLURKAPIKEY"]
    try:
        opener = urllib2.build_opener(urllib2.HTTPHandler(), urllib2.HTTPSHandler())
        return opener.open(api_url(path),urllib.urlencode(kw))
    except HTTPError, e:
        return e


