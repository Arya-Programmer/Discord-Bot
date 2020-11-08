import requests

url = "https://rapidapi.p.rapidapi.com/api/v1/search/q=elon+musk&num=13"
# url = url.format(searchedFor)

headers = {
    'x-rapidapi-host': "google-search3.p.rapidapi.com",
    'x-rapidapi-key': "e7d5b07294msh9ba660adfc5ea3ep139be4jsne13b231a609d"
}

response = requests.request("GET", url.replace(" ", "+"), headers=headers)

responseDict = dict()
responseDict = eval(response.text)

for responses in responseDict.get("results"):
    print(responses.get("title"))