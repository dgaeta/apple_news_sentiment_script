import urllib2
import json
from bs4 import BeautifulSoup
api_keys = ["76f7dbc36d0342aeafd46210b09db50177b0a3ac", "573e554a229a221c7b11d738d6d028f8005019f5", "202d04e7a07f0e72e0689fb096fba85278078e98", "6013f08a823d5cd77e688cb7354203a5d95ce3f9", "a2ec4ae758e4cf67077a7cef2a06ddf700c40553", "80e9e78b85f3fd6a77895a5ce6faddc88e4ffef6", "5086c742bf3c7c849aab9e111901760d919c2453", "4c683c8064a7493a82b059bf9cd16fa2787bfa9e", "751d591079d951f53df44ec37f24b61f153d1af8"]


def make_day_key(index):
  return 'day' + str(index)

def get_entity_data(key_index, url):
  print('making url call')
  ur='http://access.alchemyapi.com/calls/url/URLGetRankedNamedEntities?apikey=' + api_keys[key_index] +'&url='+url + '&outputMode=json' + '&sentiment=1'
  data = json.load(urllib2.urlopen(ur))
  print('url call complete')
  return data

json_file = open("DataForApple.json")
json_data = json.load(json_file)
ticker_name = json_data["Symbol"]

headlines_for_month = json_data["Headlines"]

entities_per_day = {}     

i = 0
current_api_key = api_keys[i]
day_index = 0
for news_day in headlines_for_month:
  key = make_day_key(day_index)
  for url in news_day:
    print('in loop')
    print(api_keys[i])
    data = get_entity_data(i, url)
    while(data['status'] == "ERROR" and len(data) < 3):
      print('error on url'+ str(url))
      print('changing API key from')
      print(api_keys[i])
      i+=1
      i = i%len(api_keys)
      print('to')
      print(api_keys[i])
      data = get_entity_data(i, url)
    entities_per_day.setdefault(key, []) 
    entities_per_day[key] += data['entities']
  day_index += 1


json_str = json.dumps(entities_per_day).decode('unicode-escape').encode('utf8')
with open('apple_entities_per_day2.json', 'w') as f:
  json.dump(json_str, f)





