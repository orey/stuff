import nltk

#local import
import sys
sys.path.append('.')
from no_ssl import no_ssl_verification

with no_ssl_verification():
    nltk.set_proxy('http://proxy.example.com:3128', ('', ''))
    nltk.download('popular')

