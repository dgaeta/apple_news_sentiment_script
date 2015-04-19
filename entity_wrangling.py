import urllib2
import json
from bs4 import BeautifulSoup
from StringIO import StringIO

json_file = open("apple_entities_per_day.json")
json_data = json.load(json_file)

io = StringIO(json_data)
json_obj = json.load(io)