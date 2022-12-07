from selenium import webdriver
from selenium.webdriver.common.by import By


def tiktok(username):
    global about, link
    about = None
    link = None

    chrome_options = webdriver.ChromeOptions()
    chrome_options.headless = True

    driver = webdriver.Chrome(options=chrome_options, executable_path="/Driver/chromedriver.exe")
    driver.get(f"https://tiktok.com/@{username}")


    try:
        about = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[2]/div/div[1]/h2[2]').text
    except:
        pass
    try:
        link = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[2]/div/div[1]/div[2]/a').text
    except:
        pass

    driver.quit()

    return {
        "about": about,
        "link": link
    }
