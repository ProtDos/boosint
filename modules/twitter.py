from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def twitter(username):
    global about, link, name, birthday
    about = None
    link = None
    name = None
    birthday = None
    chrome_options = webdriver.ChromeOptions()
    chrome_options.headless = True

    driver = webdriver.Chrome(options=chrome_options, executable_path="../Driver/chromedriver.exe")
    driver.get(f"https://twitter.com/{username}")

    time.sleep(5)


    try:
        about = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div/div/div/div[3]/div/div/span[1]').get_attribute("innerHTML")
    except:
        pass
    try:
        link = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div/div/div/div[4]/div/a').get_attribute('href')
    except:
        pass
    try:
        name = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div[1]/div/div[1]/div/div/span[1]/span').text
    except:
        pass
    try:
        birthday = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div/div/div/div[4]/div/span[1]').text
    except:
        pass

    driver.quit()

    return {
        "name": name,
        "link": link,
        "about": about,
        "birthday": birthday
    }

