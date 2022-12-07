import requests


def gravatar(username):
    global email_hash, photos, name, about, location, accounts
    email_hash = None
    photos = None
    name = None
    about = None
    location = None
    accounts = None
    try:
        res = requests.get(f"https://en.gravatar.com/{username}.json").json()
        r = res["entry"][0]
        try:
            email_hash = r["hash"]
        except:
            pass
        try:
            photos = []
            for item in r["photos"]:
                photos.append(item["value"])
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
            accounts = []
            for item in r["accounts"]:
                accounts.append(item["domain"])
        except:
            pass
    except:
        pass

    return {
        "name": name,
        "about": about,
        "location": location,
        "photos": photos,
        "accounts": accounts
    }
