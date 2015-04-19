import urllib2
import json
from bs4 import BeautifulSoup

api_keys = ["76f7dbc36d0342aeafd46210b09db50177b0a3ac", "573e554a229a221c7b11d738d6d028f8005019f5", "202d04e7a07f0e72e0689fb096fba85278078e98", "6013f08a823d5cd77e688cb7354203a5d95ce3f9", "a2ec4ae758e4cf67077a7cef2a06ddf700c40553", "80e9e78b85f3fd6a77895a5ce6faddc88e4ffef6", "5086c742bf3c7c849aab9e111901760d919c2453", "4c683c8064a7493a82b059bf9cd16fa2787bfa9e", "751d591079d951f53df44ec37f24b61f153d1af8"]

json_file = open("DataForApple.json")
json_data = json.load(json_file)
ticker_name = json_data["Symbol"]

headlines_for_month = json_data["Headlines"]

url_scores_dict = {} # associate a url with a sentiment score 

day_scores = []      # mean score for all articles in a day 
apple_day_scores_dict = {}

month_scores = []    # mean score for all articles in a month 
apple_month_scores_dict = {}

i = 8
current_api_key = api_keys[i]
for news_day in headlines_for_month:
  for url in news_day:
    single_day_scores = []
    while True:
      print('in loop')
      print(api_keys[i])
      print(day_scores)
      ur='http://access.alchemyapi.com/calls/url/URLGetTextSentiment?apikey=' + api_keys[i] +'&url='+url
      try:
        dat=urllib2.urlopen(ur)
        #api_error = False 
      except:
        i-=1
        if i < 0:
          break
      break
    sou=BeautifulSoup(dat)
    if sou.find('score')!=None:
      score =float(sou.find('score').string)
      url_scores_dict.setdefault(url, score)
      single_day_scores.append(score)
    if len(single_day_scores) != 0:
      day_scores.append(single_day_scores)


if len(day_scores) > 0:
  month_scores.append(sum(day_scores)/ float(len(day_scores)))


json_str = json.dumps(url_scores_dict).decode('unicode-escape').encode('utf8')
with open('apple_url_scores.json', 'w') as f:
  json.dump(json_str, f)

apple_day_scores_dict["days"] = day_scores
json_str = json.dumps(apple_day_scores_dict).decode('unicode-escape').encode('utf8')
with open('apple_day_scores.json', 'w') as f:
  json.dump(json_str, f)

apple_month_scores_dict["months"] = month_scores
json_str = json.dumps(month_scores).decode('unicode-escape').encode('utf8')
with open('apple_month_scores.json', 'w') as f:
  json.dump(json_str, f)



print("url scores")
print(url_scores_dict)
print("-----------------")
print("day_scores")
print(day_scores)
print("-----------------")
print("month_scores")
print(month_scores)



