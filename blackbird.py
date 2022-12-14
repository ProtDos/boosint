import argparse
import asyncio
import contextlib
import json
import os
import random
import subprocess
import sys
import time
import warnings
from datetime import datetime

import aiohttp
from bs4 import BeautifulSoup

file = open('data/data.json')
searchData = json.load(file)
currentOs = sys.platform
path = os.path.dirname(__file__)
warnings.filterwarnings('ignore')

useragents = open('data/useragents.txt').read().splitlines()
proxy = None


async def findUsername(username, interfaceType):
    start_time = time.time()
    timeout = aiohttp.ClientTimeout(total=10)

    #print(f"{Fore.LIGHTYELLOW_EX}[!] Searching '{username}' across {len(searchData['sites'])} social networks\033[0m")

    async with aiohttp.ClientSession(timeout=timeout) as session:
        tasks = []
        for u in searchData["sites"]:
            task = asyncio.ensure_future(makeRequest(session, u, username, interfaceType))
            tasks.append(task)

        results = await asyncio.gather(*tasks)
        now = datetime.now().strftime("%m/%d/%Y %H:%M:%S")
        executionTime = round(time.time() - start_time, 1)
        userJson = {"search-params": {"username": username, "sites-number": len(searchData['sites']), "date": now, "execution-time": executionTime}, "sites": []}
        for x in results:
            userJson["sites"].append(x)
        #pathSave = os.path.join(path, 'results', username + '.json')
        #userFile = open(pathSave, 'w')
        #json.dump(userJson, userFile, indent=4, sort_keys=True)

        #print(f"{Fore.LIGHTYELLOW_EX}[!] Search complete in {executionTime} seconds\033[0m")
        #print(f"{Fore.LIGHTYELLOW_EX}[!] Results saved to {username}.json\033[0m")
        return userJson


async def makeRequest(session, u, username, interfaceType):
    showAll = False
    url = u["url"].format(username=username)
    jsonBody = None
    useragent = random.choice(useragents)
    headers = {
        "User-Agent": useragent
    }
    metadata = []
    if 'headers' in u:
        headers |= eval(u['headers'])
    if 'json' in u:
        jsonBody = u['json'].format(username=username)
        jsonBody = json.loads(jsonBody)
    try:
        async with session.request(u["method"], url, json=jsonBody,proxy=proxy, headers=headers, ssl=False) as response:
            responseContent = await response.text()
            if 'content-type' in response.headers and "application/json" in response.headers["Content-Type"]:
                jsonData = await response.json()
            else:
                soup = BeautifulSoup(responseContent, 'html.parser')

            if not eval(u["valid"]):
                return ({"id": u["id"], "app": u['app'], "url": url, "response-status": f"{response.status} {response.reason}", "status": "NOT FOUND", "error-message": None, "metadata": metadata})
                #print(f'{Fore.LIGHTGREEN_EX}[+]\033[0m - #{u["id"]} {Fore.BLUE}{u["app"]}\033[0m {Fore.LIGHTGREEN_EX}account found\033[0m - {Fore.YELLOW}{url}\033[0m [{response.status} {response.reason}]\033[0m')
            if 'metadata' in u:
                metadata = []
                for d in u["metadata"]:
                    with contextlib.suppress(Exception):
                        value = eval(d['value']).strip('\t\r\n')
                        #print(f"   |--{d['key']}: {value}")
                        metadata.append({"type": d["type"], "key": d['key'], "value": value})
            return ({"id": u["id"], "app": u['app'], "url": url, "response-status": f"{response.status} {response.reason}", "status": "FOUND", "error-message": None, "metadata": metadata})
            #print(f'[-]\033[0m - #{u["id"]} {Fore.BLUE}{u["app"]}\033[0m account not found - {Fore.YELLOW}{url}\033[0m [{response.status} {response.reason}]\033[0m')
    except Exception as e:
        return ({"id": u["id"], "app": u['app'], "url": url, "response-status": None, "status": "ERROR", "error-message": repr(e), "metadata": metadata})


def list_sites():
    for i, u in enumerate(searchData["sites"], 1):
        print(f'{i}. {u["app"]}')


def read_results(file):
    with contextlib.suppress(Exception):
        pathRead = os.path.join(path, 'results', file)
        f = open(pathRead, 'r')
        jsonD = json.load(f)
        #print(f"Username: {jsonD['search-params']['username']}")
        #print(f'Loaded results file: {file}')
        #print(f'{Fore.WHITE}[-]\033[0m - {Fore.BLUE}{u["app"]}\033[0m account not found - {Fore.YELLOW}{u["url"]}\033[0m [{u["response-status"]}]\033[0m')
        #print('-------------------------------------------------')
        #print(f"Number of sites: {jsonD['search-params']['sites-number']}")
        #print(f"   |--{d['key']}: {d['value']}")
        #print(f'{Fore.RED}[X]\033[0m - {Fore.BLUE}{u["app"]}\033[0m error on request ({u["error-message"]}) - {Fore.YELLOW}{u["url"]}\033[0m')
        #print(f'{Fore.LIGHTGREEN_EX}[+]\033[0m - {Fore.BLUE}{u["app"]}\033[0m {Fore.LIGHTGREEN_EX}account found\033[0m - {Fore.YELLOW}{u["url"]}\033[0m [{u["response-status"]}]\033[0m')
        #print(f"Date: {jsonD['search-params']['date']}")
        #print(f'{Fore.RED}[X] Error reading file [{repr(e)}]')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='An OSINT tool to search for accounts by username in social networks.')
    parser.add_argument('-u', action='store', dest='username',
                        required=False,
                        help='The target username.')
    parser.add_argument('--list-sites', action='store_true', dest='list',
                        required=False,
                        help='List all sites currently supported.')
    parser.add_argument('-f', action='store', dest='file',
                        required=False,
                        help='Read results file.')
    parser.add_argument('--web', action='store_true', dest='web',
                        required=False,
                        help='Run webserver.')
    parser.add_argument('--proxy', action='store', dest='proxy',
                        required=False,
                        help='Proxy to send requests through.E.g: --proxy http://127.0.0.1:8080 ')
    parser.add_argument('--show-all', action='store_true', dest='showAll',
                        required=False,
                        help='Show all results.')
    arguments = parser.parse_args()

    if arguments.proxy:
        proxy = arguments.proxy
    showAll = arguments.showAll or False
    if arguments.web:
        print('[!] Started WebServer on http://127.0.0.1:9797/')
        command = subprocess.run((sys.executable, "webserver.py"))
        command.check_returncode()

    if arguments.username:
        with contextlib.suppress(Exception):
            asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
        interfaceType = 'CLI'
        asyncio.run(findUsername(arguments.username, interfaceType))
    elif arguments.list:
        list_sites()
    elif arguments.file:
        read_results(arguments.file)
