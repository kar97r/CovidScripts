import requests
import json
import  re 
import csv
#its bad practice to place your bearer token directly into the script (this is just done for illustration purposes)
BEARER_TOKEN = "AAAAAAAAAAAAAAAAAAAAAD3FPAEAAAAAqTWFoJdiLUTisWZDytmxmmJX9x8%3DQSD7wWUKGbMe38XAVJySQ7sO3BhRmT9nEYy8iWth7nwa4xmEk9"
#define search twitter function
def search_twitter(query, tweet_fields, bearer_token = BEARER_TOKEN):
    headers = {"Authorization": "Bearer {}".format(bearer_token)}

    url = "https://api.twitter.com/2/tweets/search/recent?query={}&{}".format(
        query, tweet_fields
    )
    response = requests.request("GET", url, headers=headers)

    print(response.status_code)

    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    return response.json()

#search term
query = "verified shimoga (bed OR beds OR icu OR oxygen OR ventilator OR ventilators)"
#twitter fields to be returned by api call
tweet_fields = "tweet.fields=text,created_at"

#twitter api call
json_response = search_twitter(query=query, tweet_fields=tweet_fields, bearer_token=BEARER_TOKEN)
#pretty printing
datalist = json_response["data"]
count = 1

fi =  open('Covid-Resources.csv', 'w', newline='')
writer = csv.writer(fi)
        
writer.writerow(["SN", "Tweet", "Created At","Phone"])
for i in datalist:
    # twst = i["text"]
    if "RT" not in i["text"]:
        fin = i["created_at"].replace("T"," ").replace("Z"," ")
        phone = re.search(r'\b[789]\d{9}\b', i["text"], flags=0)
        if phone:
            phone = (phone.group(0))
        writer.writerow([count, i["text"], fin, phone])
        print(count,fin , i["text"] , phone)
        
        
        count = count +1
