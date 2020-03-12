import sys
import requests
import base64
import json
import logging
import time

client_id = "2cfc425c82da43f5bb1fa4f31d76898b**"
client_secret = "03e255dd9ee54d9f917d2a5cfde1d7f6**"


def main():
    headers = get_headers(client_id, client_secret)

    # Spotify Search API
    params = {
        "q": "BTS",
        "type": "artist",
        # "limit": 5
    }

    r = requests.get("https://api.spotify.com/v1/search",params=params, headers=headers)
    # print(r.text)
    # sys.exit(0)

    try:
        r = requests.get("https://api.spotify.com/v1/search",params=params, headers=headers)
    except:
        logging.error(r.text)
        sys.exit(1)

    r = requests.get("https://api.spotify.com/v1/search",params=params, headers=headers)

    if r.status_code != 200:
        logging.error(r.text)

        if r.status_code == 429:

            retry_after = json.loads((r.headers)['Retry-After'])
            time.sleep(int(retry_after))
            r = requests.get("https://api.spotify.com/v1/search", params=params, headers=headers)

        elif r.status_code == 401:

            headers = get_headers(client_id, client_secret)
            r = requests.get("https://api.spotify.com/v1/search", params=params, headers=headers)
        else:
            sys.exit(1)

    r = requests.get("https://api.spotify.com/v1/artists/3Nrfpe0tUJi4K4DXYWgMUX/albums", params=params, headers=headers)

    raw = json.loads(r.text)

    total = raw['total']
    offset = raw['offset']
    limit = raw['limit']
    next = raw['next']

    # print(total)
    # print(offset)
    # print(limit)
    # print(next)
    # sys.exit(1)

    albums = []

    print(len(raw['items']))
    albums.extend(raw['items'])
    # print(len(albums))
    # sys.exit(1)

    # 100개를 뽑아옴
    count = 0
    while count < 100 and next:

        r = requests.get(raw['next'], headers=headers)
        raw = json.loads(r.text)
        next = raw['next']
        print(next)

        albums.extend(raw['items'])
        count = len(albums)
    print(len(albums))

def get_headers(cleint_id, client_secret):
    endpoint = "https://accounts.spotify.com/api/token"
    encoded = base64.b64encode("{}:{}".format(client_id, client_secret).encode('utf-8')).decode('ascii')

    headers = {
        "Authorization": "Basic {}".format(encoded)
    }

    payload = {
        "grant_type": "client_credentials"
    }

    r = requests.post(endpoint, data=payload, headers=headers)
    # print(r.status_code)
    # print(r.text)
    # print(r.headers)
    # sys.exit(0)


    access_token = json.loads(r.text)['access_token']

    headers = {
        "Authorization": "Bearer {}".format(access_token)
    }

    return headers

if __name__ == '__main__':
    main()