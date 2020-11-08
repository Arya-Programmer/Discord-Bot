from googleapiclient.discovery import build
import requests

scopes = "https://www.googleapis.com/youtube/v3/search"

def main():

    youtube = build("youtube", 'v3', developerKey=api_key)

    params = {
        "part": 'snippet',
        "q": 'learn python',
        "key": api_key,
        'max_results': 10
    }
    r = requests.get(scopes, params=params)
    print(r.json().get('items')[0]['id']['videoId'])
    print(r.json())
    for i in r.json().get('items'):
        if i['id'] and i['id']['kind'] == 'youtube#video':
            print(i['id']['videoId'])


    # print(response)

if __name__ == "__main__":
    main()