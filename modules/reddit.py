from selenium import webdriver
from selenium.webdriver.common.by import By


def reddit(username):
    global about, link
    about = None
    link = None

    chrome_options = webdriver.ChromeOptions()
    chrome_options.headless = True

    driver = webdriver.Chrome(options=chrome_options, executable_path="/Driver/chromedriver.exe")
    driver.get(f"https://www.reddit.com/user/{username}")

    try:
        about = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div[2]/div/div[1]/div/div[3]').get_attribute("innerHTML")
    except:
        pass
    try:
        link = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div[2]/div/div[1]/div/div[5]').get_attribute("innerHTML")
    except:
        pass

    return {
        "about": about,
        "link": link
    }