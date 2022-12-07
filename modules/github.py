from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def github(username):
    global about, link, name, location
    chrome_options = webdriver.ChromeOptions()
    chrome_options.headless = True

    driver = webdriver.Chrome(options=chrome_options, executable_path="/Driver/chromedriver.exe")
    driver.get(f"https://github.com/{username}")

    time.sleep(5)

    about = None
    link = None
    name = None
    location = None

    try:
        data = driver.find_element(By.XPATH,
                                   '/html/body/div[4]/main/div[2]/div/div[1]/div/div[2]/div[2]/div[2]/div[1]/div').get_attribute("innerHTML")
        about = data
    except:
        pass
    try:
        data = driver.find_element(By.XPATH,
                                   '/html/body/div[4]/main/div[2]/div/div[1]/div/div[2]/div[2]/div[2]/ul/li[2]/a').get_attribute(
            'innerHTML')
        link = data
    except:
        pass
    try:
        data = driver.find_element(By.XPATH,
                                   '/html/body/div[4]/main/div[2]/div/div[1]/div/div[2]/div[1]/div[2]/h1/span[2]').get_attribute("innerHTML")
        name = data
    except:
        pass
    try:
        data = driver.find_element(By.XPATH,
                                   '/html/body/div[4]/main/div[2]/div/div[1]/div/div[2]/div[2]/div[2]/ul/li[1]/span').get_attribute("innerHTML")
        location = data
    except:
        pass

    driver.quit()

    return {
        "name": name,
        "about": about,
        "link": link,
        "location": location
    }
