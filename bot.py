import urllib2
import json
term = 'seattle'
print json.load(urllib2.urlopen("http://api.urbandictionary.com/v0/define?term=" + term))["list"][0]
