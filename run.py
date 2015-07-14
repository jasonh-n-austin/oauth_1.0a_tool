import json
import requests
import logging
import requests_cache
#requests_cache.install_cache('pbs-api-cache', backend='sqlite', expire_after=300, allowable_codes=(200,))
from rauth.session import OAuth1Session
#from rauth.service import OAuth1Service
import ConfigParser

config = ConfigParser.RawConfigParser()
config.read('config.ini')
CONSUMER_KEY = config.get('paperbackswap', 'consumer_key')
CONSUMER_SECRET = config.get('paperbackswap', 'consumer_secret')
ACCESS_TOKEN = config.get('paperbackswap', 'access_token')
ACCESS_SECRET = config.get('paperbackswap', 'access_secret')

try:
    import http.client as http_client
except ImportError:
    # Python 2
    import httplib as http_client
http_client.HTTPConnection.debuglevel = 1

# You must initialize logging, otherwise you'll not see debug output.
logging.basicConfig() 
logging.getLogger().setLevel(logging.DEBUG)
requests_log = logging.getLogger("requests.packages.urllib3")
requests_log.setLevel(logging.DEBUG)
requests_log.propagate = True

session = OAuth1Session(consumer_key=CONSUMER_KEY,
	consumer_secret=CONSUMER_SECRET,
	access_token=ACCESS_TOKEN,
	access_token_secret=ACCESS_SECRET)

#r = session.get("http://www.paperbackswap.com/api/v2/index.php?RequestType=ISBNList&ISBN=9780812515282");
r = session.get("http://www.paperbackswap.com/api/v2/index.php?RequestType=ClubWishList&ISBN=9780812515282&fields=Wishes");
#print "Cached? %s" % (r.from_cache)
print json.dumps(r.json(), sort_keys=True, indent=4, separators=(',', ': '))


#service = OAuth1Service(
#           name='PBS',
#           consumer_key=CONSUMER_KEY,
#           consumer_secret=CONSUMER_SECRET,
#           request_token_url='http://www.paperbackswap.com/api/request_token.php',
#           access_token_url='http://www.paperbackswap.com/api/authorize.php',
#           authorize_url='http://www.paperbackswap.com/api/access_token.php',
#           base_url='http://www.paperbackswap.com/api/v2/index.php')
