"""
    gets spotify account data
"""
import os
import json
from sys import argv
from rich import print as rprint

try:
    PRINTS = argv[1]
except IndexError:
    PRINTS = False

files = [
    "Follow.json",
    "Identifiers.json",
    "Inferences.json",
    "Payments.json",
    "Playlist1.json",
    "Playlist2.json",
    "PodcastInteractivityRatedShow.json",
    "SearchQueries.json",
    "StreamingHistory0.json",
    "StreamingHistory1.json",
    "StreamingHistory2.json",
    "StreamingHistory3.json",
    "StreamingHistory4.json",
    "Userdata.json",
    "YourLibrary.json",
]


def replace_last(string, delimiter, replacement):
    """
    replaces the last delimiter in a string with a replacement
    """
    start, _, end = string.rpartition(delimiter)
    return f"{start.upper()}{replacement}{end.upper()}"


def get(name: str):
    """
    gets the name of an index from a list
    """
    if not name.endswith(".json"):
        name += ".json"
    if name in files:
        return os.path.join("files", files[files.index(name)])
        #return f"files/{files[files.index(name)]}"
    raise IndexError


def load(file):
    """
    loads a json file
    """
    return json.load(file)


with open(get("Userdata"), "r", encoding="utf-8") as f:
    data = load(f)

    creation_date = data["creationTime"]
    username = data["username"]
    email = data["email"]
    birthdate = data["birthdate"]
    gender = data["gender"]
    facebook_creation = data["createdFromFacebook"]
    country = data["country"]
    phone_number = data["mobileNumber"]

with open(get("Playlist1"), "r", encoding="utf-8") as f:
    data = load(f)
    playlist_amount = len(data["playlists"])

with open(get("Follow"), "r", encoding="utf-8") as f:
    data = load(f)
    followers = data["followingUsersCount"]
    following = data["followerCount"]

with open(get("SearchQueries"), "r", encoding="utf-8") as f:
    data = load(f)
    dat = json.dumps(data, indent=4)
    i = 0
    platforms:list = list(dict.fromkeys([dat["platform"] for dat in data]))

if __name__ == "__main__":
    platforms.remove("")
    last_elem_len = len(platforms[-1])
    PRETTY_PLATFORMS = ", ".join(platforms).lower()
    PRETTY_PLATFORMS = replace_last( PRETTY_PLATFORMS, ", ", " and ")
    if not PRINTS:
        rprint(f"Account Created on {creation_date}")
        rprint(f"Birthdate: {birthdate}")
        rprint(f"gender: {gender}")
        rprint(f"country: {country}")
        rprint(f"Created From Facebook: {facebook_creation}")
        rprint(f"username: {username}")
        rprint(f"Email: {email}")
        rprint(f"Phone Number: {phone_number}")
        rprint(f"{playlist_amount} Playlists")
        rprint(f"{following} Accounts Follow You")
        rprint(f"You Follow {followers} Accounts")
        rprint(f"You Use Spotify on {PRETTY_PLATFORMS}")
