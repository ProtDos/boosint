import contextlib
import requests


def gravatar(username):
    global email_hash, photos, name, about, location, accounts
    email_hash = None
    photos = None
    name = None
    about = None
    location = None
    accounts = None
    with contextlib.suppress(Exception):
        res = requests.get(f"https://en.gravatar.com/{username}.json").json()
        r = res["entry"][0]
        with contextlib.suppress(Exception):
            email_hash = r["hash"]
        with contextlib.suppress(Exception):
            photos = [item["value"] for item in r["photos"]]
        with contextlib.suppress(Exception):
            name = r["name"]["formatted"]
        with contextlib.suppress(Exception):
            about = r["aboutMe"]
        try:
            location = r["currentLocation"]
        except Exception:
            pass
        try:
            accounts = [item["domain"] for item in r["accounts"]]
        except:
            pass
    return {
        "name": name,
        "about": about,
        "location": location,
        "photos": photos,
        "accounts": accounts
    }
