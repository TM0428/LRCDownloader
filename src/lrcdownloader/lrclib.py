import requests

BASE_URL = "https://lrclib.net"


def search_lyrics(q):
    url = f"{BASE_URL}/api/search?q={q}"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()


def main():
    lrcs = search_lyrics("Only My Railgun")
    for lrc in lrcs:
        print(lrc["artistName"], lrc["trackName"])
