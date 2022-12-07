from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def pin(username):
    global about, name
    about = None
    name = None
    chrome_options = webdriver.ChromeOptions()
    chrome_options.headless = True

    driver = webdriver.Chrome(options=chrome_options, executable_path="/Driver/chromedriver.exe")
    driver.get(f"https://pinterest.com/{username}")

    time.sleep(5)
    try:
        about = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div/div[1]/div[2]/div/div[1]/div[1]/div/div[4]/div/div/div/div/div/span').get_attribute("innerHTML")
    except:
        pass
    try:
        name = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div/div[1]/div[2]/div/div[1]/div[1]/div/div[2]/div/h1/div').text
    except:
        pass

    return {
        "name": name,
        "about": about
    }
