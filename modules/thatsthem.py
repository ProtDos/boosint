import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
import time


def thatsthem(username, method="email"):
    username = username[0]
    username.replace(" ", "-")
    result = []
    options = uc.ChromeOptions()
    options.headless = True
    driver = uc.Chrome(options=options)

    try:
        if method == "name":
            thatsthem_user_search(driver, "https://thatsthem.com/people-search", '/html/body/div/main/section[1]/div/div/div/form/div/input[1]', username)

            for i in range(20):
                try:
                    name = driver.find_element(By.XPATH, f'/html/body/div/main/div/div[2]/div[2]/div[2]/div[{i}]/div/div[1]/div[2]').text
                except Exception:
                    name = None
                try:
                    location = driver.find_element(By.XPATH, f'/html/body/div/main/div/div[2]/div[2]/div[2]/div[{i}]/div/div[1]/div[3]').text
                except Exception:
                    location = None
                try:
                    gender = driver.find_element(By.XPATH, f'/html/body/div/main/div/div[2]/div[2]/div[2]/div[{i}]/div/div[1]/div[2]/span/i').get_attribute("data-title")
                except Exception:
                    gender = None
                try:
                    age = driver.find_element(By.XPATH, f'/html/body/div/main/div/div[2]/div[2]/div[2]/div[{i}]/div/div[1]/div[4]').text
                except Exception:
                    age = None
                try:
                    s = driver.find_element(By.XPATH, f'/html/body/div/main/div/div[2]/div[2]/div[2]/div[{i}]/div/div[2]/div[3]').get_attribute("innerHTML")
                    a = s.split('class="web">\n')
                    phones = [item.replace("</a>", "").split("\n")[0] for item in a if "</a>" in item]

                except Exception:
                    phones = None
                try:
                    emails = driver.find_element(By.XPATH, f'/html/body/div/main/div/div[2]/div[2]/div[2]/div[{i}]/div/div[2]/div[4]').get_attribute("innerHTML")
                except Exception:
                    emails = None
                try:
                    ips = driver.find_element(By.XPATH, f'/html/body/div/main/div/div[2]/div[2]/div[2]/div[{i}]/div/div[3]/div/div[1]/div').get_attribute("innerHTML")
                except Exception:
                    ips = None

                js = {
                    "name": name,
                    "location": location,
                    "gender": gender,
                    "age": age,
                    "phones": phones,
                    "emails": emails,
                    "ips": ips
                }

                if js["name"] != None:
                    result.append(js)
        elif method == "email":
            thatsthem_user_search(driver, "https://thatsthem.com/reverse-email-lookup", '/html/body/div/main/section[1]/div/div/div/form/div/input', username)

            for i in range(20):
                try:
                    name = driver.find_element(By.XPATH,
                                               f'/html/body/div/main/div/div[2]/div[2]/div[1]/div[{i}]/div/div[1]/div[2]').text
                except Exception:
                    name = None
                try:
                    location = driver.find_element(By.XPATH,
                                                   f'/html/body/div/main/div/div[2]/div[2]/div[1]/div[{i}]/div/div[1]/div[3]').text
                except Exception:
                    location = None
                try:
                    gender = driver.find_element(By.XPATH,
                                                 f'/html/body/div/main/div/div[2]/div[2]/div[1]/div[{i}]/div/div[1]/div[2]/span/i').get_attribute(
                        "data-title")
                except Exception:
                    gender = None
                try:
                    age = driver.find_element(By.XPATH,
                                              f'/html/body/div/main/div/div[2]/div[2]/div[1]/div[{i}]/div/div[1]/div[4]').text
                except Exception:
                    age = None
                try:
                    s = driver.find_element(By.XPATH,
                                            f'/html/body/div/main/div/div[2]/div[2]/div[1]/div[{i}]/div/div[2]/div[2]').get_attribute(
                        "innerHTML")
                    a = s.split('class="web">\n')
                    phones = [item.replace("</a>", "").split("\n")[0] for item in a if "</a>" in item]

                except Exception:
                    phones = None
                try:
                    emails = driver.find_element(By.XPATH,
                                                 f'/html/body/div/main/div/div[2]/div[2]/div[1]/div[{i}]/div/div[2]/div[3]').get_attribute(
                        "innerHTML")
                except Exception:
                    emails = None

                js = {
                    "name": name,
                    "location": location,
                    "gender": gender,
                    "age": age,
                    "phones": phones,
                    "emails": emails,
                }

                if js["name"] != None:
                    result.append(js)
        elif method == "phone":
            thatsthem_user_search(driver, "https://thatsthem.com/reverse-phone-lookup", '/html/body/div/main/section[1]/div/div/div/form/div/input', username)

            for i in range(20):
                try:
                    name = driver.find_element(By.XPATH,
                                               f'/html/body/div/main/div/div[2]/div[2]/div[2]/div[{i}]/div/div[1]/div[2]').text
                except Exception:
                    name = None
                try:
                    location = driver.find_element(By.XPATH,
                                                   f'/html/body/div/main/div/div[2]/div[2]/div[2]/div[{i}]/div/div[1]/div[3]').text
                except:
                    location = None
                try:
                    gender = driver.find_element(By.XPATH,
                                                 f'/html/body/div/main/div/div[2]/div[2]/div[2]/div[{i}]/div/div[1]/div[2]/span/i').get_attribute(
                        "data-title")
                except:
                    gender = None
                try:
                    age = driver.find_element(By.XPATH,
                                              f'/html/body/div/main/div/div[2]/div[2]/div[2]/div[{i}]/div/div[1]/div[4]').text
                except:
                    age = None
                try:
                    s = driver.find_element(By.XPATH,
                                            f'/html/body/div/main/div/div[2]/div[2]/div[2]/div[{i}]/div/div[2]/div[2]').get_attribute(
                        "innerHTML")
                    a = s.split('class="web">\n')
                    phones = [item.replace("</a>", "").split("\n")[0] for item in a if "</a>" in item]

                except:
                    phones = None
                try:
                    try:
                        emails = driver.find_element(By.XPATH,
                                                     f'/html/body/div/main/div/div[2]/div[2]/div[2]/div[{i}]/div/div[2]/div[4]').get_attribute(
                            "innerHTML")
                    except:
                        emails = driver.find_element(By.XPATH,
                                                     f'/html/body/div/main/div/div[2]/div[2]/div[2]/div[{i}]/div/div[2]/div[3]').get_attribute(
                            "innerHTML")
                except:
                    emails = None

                js = {
                    "name": name,
                    "location": location,
                    "gender": gender,
                    "age": age,
                    "phones": phones,
                    "emails": emails,
                }

                if js["name"] != None:
                    result.append(js)
        else:
            return {
                "bitch"
            }

        return result
    except Exception:
        return {
            "name": "",
            "location": "",
            "gender": "",
            "age": "",
            "phones": "",
            "emails": "",
            "ips": ""
        }


def thatsthem_user_search(driver, xpath1, xpath2, username):
    """Function that: searches for users matching username

    Args:
        driver (driver): the driver that is used to search
        xpath1 (str): xpath of the first result
        xpath2 (str): xpath of the second result
        username (str): username of the user
    """    
    driver.get(xpath1)
    time.sleep(5)
    driver.find_element(By.XPATH, xpath2).send_keys(username)
    time.sleep(0.5)
    driver.find_element(By.XPATH, '/html/body/div/main/section[1]/div/div/div/form/div/button').click()
    time.sleep(5)
