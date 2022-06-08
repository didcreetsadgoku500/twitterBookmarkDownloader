import requests
import json

bearerToken = "BEARER_TOKEN_HERE"
headers = {"Authorization": f"Bearer {bearerToken}"}


raw = open('bookmarks.json')
bookmarksJSON = json.load(raw)


def getIDfromJSON(mozillaContainer):
    for i in mozillaContainer["children"]:
        if (i["type"] == "text/x-moz-place"): #is bookmark
            if "twitter.com" in i["uri"].lower():
                if "status/" in i["uri"].lower():
                    j = i["uri"].lower().split("status/")[1].split("?")[0]
                    date = str(i["id"]) + "_" + str(i["dateAdded"])
                    processTweet(j, date)
            else:
                print("You're not a twitter link!")
        elif (i["type"] == "text/x-moz-place-container"): #is subfolder
            getIDfromJSON(i)

def processTweet(id, date):
    compositeUrl = f"https://api.twitter.com/2/tweets/{id}?expansions=attachments.media_keys&media.fields=url"
    r = requests.get(compositeUrl, headers=headers)
    data = r.json()
    if "includes" in data:
        if "media" in data["includes"]:
            mediaArray = data["includes"]["media"]
            for media in mediaArray:
                if (media["type"] == "photo"):
                    downloadImage(media["url"], date)


def downloadImage(img, date):
    file_name = str(date) + "_" + img.split('/')[-1]
    r = requests.get(img, stream=True)
    if r.status_code == 200:
        with open(file_name, 'wb') as f:
            for chunk in r:
                f.write(chunk)
    else:
        print(f"ERROR: Could not download {img}")

getIDfromJSON(bookmarksJSON)