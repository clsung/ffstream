import os
import urllib
import urllib2

def callAPI(path, **kw):
    api_url= lambda x: 'http://www.plurk.com/API%s' % x
    if 'api_key' not in kw.keys(): kw['api_key'] = os.environ["PLURKAPIKEY"]
    opener = urllib2.build_opener(urllib2.HTTPHandler(), urllib2.HTTPSHandler())
    return opener.open(api_url(path),urllib.urlencode(kw))


