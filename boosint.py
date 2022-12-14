from blackbird import findUsername
import asyncio
import contextlib
import os
import shutil
import requests
from os import listdir
from os.path import isfile, join
import json
import argparse
import threading
import time
import pathlib

working = []
done = False


def find_website(username):
    global done
    with open("data/domain-endings.txt", "r") as file:
        content = file.read().split("\n")
    for ending in content:
        with contextlib.suppress(Exception):
            out = requests.get(f"http://{username}.{ending}").status_code
            if out == 200:
                working.append(f"http://{username}.{ending}")
    done = True


if __name__ == "__main__":
    try:
        parser = argparse.ArgumentParser(
            prog='BoOSINT',
            description='A powerful username OSINT tool.',
            epilog='Create an issue for help')
        parser.add_argument("username", help="Username of the target")
        parser.add_argument("-o", "--output", required=False, default="report.json", help="Enter the output filename for the report.")
        parser.add_argument("-t", "--type", required=False, default="json", choices=["json", "txt"], help="Choose what type of report you want.")
        args = parser.parse_args()

        username = args.username
        output = args.output
        typ = args.type

        if not output.endswith(".json"):
            exit("Please declare a file with .json as ending.")


        ############################### MAIGRET ###############################
        print("[i] Started using maigret. Please stand by.")
        if os.path.isdir("reports"):
            shutil.rmtree("reports")
        input("<")
        try:
            cur_ = pathlib.Path(__file__).parent.resolve()
            os.system(f"cd {cur_} && maigret -J simple {username}")
        except Exception:
            pass
        os.system("cls")
        os.system("clear")
        print("[+] Done with maigret.")
        ############################### GitRecon ###############################
        print("[i] Starting GitRecon.")
        try:
            from GitRecon.gitrecon import gitrecon
            gitrec = gitrecon(username)
        except:
            print("[-] Your github auth token is invalid. Please make a new one in the config file.")
        print("[+] GitRecon has finished.")
        ############################### Blackbird ###############################
        print("[i] Starting Blackbird.")
        try:
            asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
        except:
            pass
        out = asyncio.run(findUsername(username, "CLI"))


        valid = []

        for site in out["sites"]:
            if site["status"] == "FOUND":
                valid.append(site)
        print("[+] Done.")
        ############################### OtherOSINT ###############################
        ## Find possible websites
        threading.Thread(target=find_website, args=(username,))
        print("[+] Finding possible websites.")
        ## Social Media
        from modules import reddit, pinterest, tiktok, twitter, github, gravatar, scratch

        git = github.github(username)
        print("[+] GitHub")
        grav = gravatar.gravatar(username)
        print("[+] Gravatar")
        pin = pinterest.pin(username)
        print("[+] Pinterest")
        red = reddit.reddit(username)
        print("[+] Reddit")
        scr = scratch.scratch(username)
        print("[+] Scratch")
        tik = tiktok.tiktok(username)
        print("[+] TikTok")
        twi = twitter.twitter(username)
        print("[+] Twitter")
        ## Get Other Info
        from modules.get_info import gmail, yahoo, hotmail
        gma = gmail(username)
        print("[+] Gmail")
        yah = yahoo(username)
        print("[+] Yahoo")
        hot = hotmail(username)
        print("[+] Hotmail")
        ############################### Final ###############################
        maigret_out = [f for f in listdir("reports") if isfile(join("reports", f))]
        with open(f"reports\\report_{username}_simple.json", "r") as file:
            maigret_json = json.load(file)
        alibis = []
        for item in maigret_out:
            if str(item) != f"reports\\report_{username}_simple.json":
                alibis.append(item.split("report_")[1].split("_simple.json")[0])
        print("[+] Alibis")

        ############################### ThatsThem ###############################
        try:
            gitrec["name"]
        except:
            gitrec = {
                "name": None,
                "leaked_emails": None,
                "bio": None,
                "location": None
            }


        from modules.thatsthem import thatsthem
        # Name
        thats_them_name1 = thatsthem([gitrec["name"] if gitrec["name"] != None else ""], method="name")
        thats_them_name2 = thatsthem([git["name"] if git["name"] != None else ""], method="name")
        thats_them_name3 = thatsthem([grav["name"] if grav["name"] != None else ""], method="name")
        thats_them_name4 = thatsthem([pin["name"] if pin["name"] != None else ""],method="name")
        thats_them_name5 = thatsthem([twi["name"] if twi["name"] != None else ""], method="name")
        # Email
        thats_them_email1 = thatsthem([hot["email"] if hot["email"] != None else ""], method="email")
        thats_them_email2 = thatsthem([gitrec["leaked_emails"] if gitrec["leaked_emails"] != None else ""], method="email")

        print("[i] Waiting for websites.")
        while True:
            if done:
                break
            time.sleep(10)
        print("[+] Done")

        final_result = {
            "Main": [
                {
                    "username": username,
                    "name": [[gitrec["name"] if gitrec["name"] != None else ""], [git["name"] if git["name"] != None else ""], [grav["name"] if grav["name"] != None else ""], [pin["name"] if pin["name"] != None else ""], [twi["name"] if twi["name"] != None else ""]],
                    "emails": [[hot["email"] if hot["email"] != None else ""], [gitrec["leaked_emails"] if gitrec["leaked_emails"] != None else ""]],
                    "abouts": [[gitrec["bio"] if gitrec["bio"] != None else ""], [git["about"] if git["about"] != None else ""], [grav["about"] if grav["about"] != None else ""], [scr["about2"] if scr["about2"] != None else ""], [pin["about"] if pin["about"] != None else ""], [red["about"] if red["about"] != None else ""], [scr["about"] if scr["about"] != None else ""], [tik["about"] if scr["about"] != None else ""], [twi["about"] if twi["about"] != None else ""]],
                    "location": [[gitrec["location"] if gitrec["location"] != None else ""], [grav["location"] if grav["location"] != None else ""]],
                    "birthday": twi["birthday"],
                    "phone": [[gma["phone"] if gma["phone"] != None else ""], [yah["phone"] if yah["phone"] != None else ""]],
                    "device": gma["model"],
                    "websites": [[twi["link"] if twi["link"] != None else ""], [tik["link"] if tik["link"] != None else ""], [git["link"] if git["link"] != None else ""]],
                    "socials": [[l["app"] for l in valid], [social for social in maigret_json]],
                    "alibis": [ali for ali in alibis],
                    "other_possible_websites": [site for site in working]
                }
            ]
        }

        ThatsThemResult = {
            "ThatsThem": [
                {
                    "name": [thats_them_name1["name"], thats_them_name2["name"], thats_them_name3["name"], thats_them_name4["name"], thats_them_name5["name"], thats_them_email1["name"], thats_them_email2["name"]],
                    "location": [thats_them_name1["location"], thats_them_name2["location"], thats_them_name3["location"], thats_them_name4["location"], thats_them_name5["location"], thats_them_email1["location"], thats_them_email2["location"]],
                    "gender": [thats_them_name1["gender"], thats_them_name2["gender"], thats_them_name3["gender"], thats_them_name4["gender"], thats_them_name5["gender"], thats_them_email1["gender"], thats_them_email2["gender"]],
                    "age": [thats_them_name1["age"], thats_them_name2["age"], thats_them_name3["age"], thats_them_name4["age"], thats_them_name5["age"], thats_them_email1["age"], thats_them_email2["age"]],
                    "phones": [thats_them_name1["phones"], thats_them_name2["phones"], thats_them_name3["phones"], thats_them_name4["phones"], thats_them_name5["phones"], thats_them_email1["phones"], thats_them_email2["phones"]],
                    "emails": [thats_them_name1["emails"], thats_them_name2["emails"], thats_them_name3["emails"], thats_them_name4["emails"], thats_them_name5["emails"], thats_them_email1["emails"], thats_them_email2["emails"]],
                }
            ]
        }

        print("[i] Generating report.")

        if typ == "json":
            with open(output, "w") as file:
                json.dump(final_result, file, indent=4)
                json.dump(ThatsThemResult, file, indent=4)
        elif typ == "txt":
            with open(output, "w") as file:
                file.write("BoOSINT Results\n\n")
                file.write(f"Report for {username}\n")

                file.write(f"Possible Names: {final_result['Main'][0]['name']}\n")
                file.write(f"Possible Names #2: {ThatsThemResult['ThatsThem'][0]['name']}\n\n")

                file.write(f"Possible Location: {final_result['Main'][0]['location']}\n")
                file.write(f"Possible Location #2: {ThatsThemResult['ThatsThem'][0]['location']}\n\n")

                file.write(f"Possible Gender: {ThatsThemResult['ThatsThem'][0]['gender']}\n\n")

                file.write(f"Possible Emails: {final_result['Main'][0]['emails']}\n")
                file.write(f"Possible Emails #2: {ThatsThemResult['ThatsThem'][0]['emails']}\n\n")

                file.write(f"Possible Phones: {final_result['Main'][0]['phone']}\n")
                file.write(f"Possible Phones #2: {ThatsThemResult['ThatsThem'][0]['phones']}\n\n")

                file.write(f"Possible Birthday: {final_result['Main'][0]['birthday']}\n")
                file.write(f"Possible Age: {ThatsThemResult['ThatsThem'][0]['age']}\n\n")

                file.write(f"Possible AboutMe's: {final_result['Main'][0]['abouts']}\n\n")

                file.write(f"Possible Devices: {final_result['Main'][0]['device']}\n\n")

                file.write(f"Possible Websites: {final_result['Main'][0]['websites']}\n")
                file.write(f"Possible Websites #2: {final_result['Main'][0]['other_possible_websites']}\n\n")

                file.write(f"Possible Socials: {final_result['Main'][0]['socials']}\n\n")

                file.write(f"Possible Alibis: {final_result['Main'][0]['alibis']}\n\n")

                file.write("-"*20 + "END OF REPORT" + "-"*20)
    except KeyboardInterrupt:
        exit("Ctrl+C detected. Exitting.")
    print("Report is finished.")

