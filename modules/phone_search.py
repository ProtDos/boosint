from ScrapeSearchEngine.SearchEngine import *


def search_phone(number):
    results = []
    search = f'\"{number}\"'
    try:
        googleText, googleLink = Google(search=search,
                                        userAgent="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.96 Safari/537.36")

        results.extend(iter(googleLink))
        return results

    except Exception:
        return {
            "status": "error"
        }
