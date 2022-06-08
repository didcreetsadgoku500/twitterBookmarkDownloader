# Twitter / Firefox Bookmark Downloader

This Python script flips through your exported Firefox bookmarks and downloads any tweet it finds with an image.

You must replace "BEARER_TOKEN_HERE" with your Twitter API bearer token. You can get one of those by following the instructions [here](https://developer.twitter.com/en/docs/authentication/oauth-2-0/bearer-tokens)

In Firefox, go to Manage Bookmarks -> Export... and save the JSON file as "bookmarks.json". Place it in the same directory as the Python script and run the Python script.

If you dont wanna search all your bookmarks, you can pick a child of type "text/x-moz-place-container" and just make that your bookmarks.json

Tested with Python 3.8.2
