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
        try:
            email_hash = r["hash"]
        except Exception:
            pass
        try:
            photos = [item["value"] for item in r["photos"]]
        except:
            pass
        try:
            name = r["name"]["formatted"]
        except:
            pass
        try:
            about = r["aboutMe"]
        except:
            pass
        try:
            location = r["currentLocation"]
        except:
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
