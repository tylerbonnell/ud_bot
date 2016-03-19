import urllib2
import json
term = "yeltsin"
term = term.replace(" ", "%20")
req = json.load(urllib2.urlopen("http://api.urbandictionary.com/v0/define?term=" + term))["list"]
if len(req) > 0:
    print req[0]
else:
    print "No results found!"
