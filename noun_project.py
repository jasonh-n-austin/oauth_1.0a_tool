import logging
import requests
import requests_cache
requests_cache.install_cache()
from rauth.session import OAuth1Session
import ConfigParser

config = ConfigParser.RawConfigParser()
config.read('config.ini')
CONSUMER_KEY = config.get('noun_project', 'consumer_key')
CONSUMER_SECRET = config.get('noun_project', 'consumer_secret')

session = OAuth1Session(consumer_key=CONSUMER_KEY,
        consumer_secret=CONSUMER_SECRET)


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

response = session.get("http://api.thenounproject.com/icon/1");
print response.from_cache
print response.json()
#import requests
#import requests_cache

#requests_cache.install_cache()
