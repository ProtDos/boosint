import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def gmail(username):
    global model, phone
    model = None
    phone = None
    options = uc.ChromeOptions()
    driver = uc.Chrome(options=options)

    driver.get("https://accounts.google.com/login")

    time.sleep(0.5)

    driver.find_element(By.XPATH,
                                '/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input').send_keys(
        username)

    time.sleep(0.5)

    try:

        driver.find_element(By.XPATH,
                                  '/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[2]/div/div[1]/div/div/button').click()

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[2]/div/div[2]/div/div/button"))
        )

        time.sleep(5)

        driver.find_element(By.XPATH,
                                     '/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[2]/div/div[2]/div/div/button').click()

        time.sleep(5)

        model = driver.find_element(By.XPATH,
                                    '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/section/header/div/h2/span').text

        driver.find_element(By.XPATH,
                                    '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div[2]/div[2]/div/div/button').click()

        time.sleep(5)

        tel = driver.find_element(By.XPATH,
                                  '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/span/span').text

        phone = tel

    except:
        pass
    driver.quit()
    return {
        "model": model,
        "phone": phone
    }


def yahoo(username):
    global phone
    phone = None
    options = uc.ChromeOptions()
    driver = uc.Chrome(options=options)

    driver.get("https://login.yahoo.com/")

    try:

        driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div[2]/div[2]/form/div[1]/div[3]/input').send_keys(username)

        time.sleep(0.5)

        driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div[2]/div[2]/form/div[2]').click()

        time.sleep(0.5)

        driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div[2]/div[2]/form/div[4]/input').click()

        time.sleep(5)

        phone = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div[2]/div[2]/form/ul/li[2]').get_attribute("data-display")

    except:
        pass
    driver.quit()
    return {
        "phone": phone
    }


def hotmail(username):
    global email
    email = None
    options = uc.ChromeOptions()
    driver = uc.Chrome(options=options)

    driver.get("https://login.live.com/login.srf")

    try:

        driver.find_element(By.XPATH, '/html/body/div[1]/form[1]/div/div/div[2]/div[1]/div/div/div/div/div[1]/div[3]/div/div/div/div[2]/div[2]/div/input[1]').send_keys(username)

        time.sleep(0.5)

        driver.find_element(By.XPATH, '/html/body/div[1]/form[1]/div/div/div[2]/div[1]/div/div/div/div/div[1]/div[3]/div/div/div/div[4]/div/div/div/div/input').click()

        time.sleep(0.5)

        driver.find_element(By.XPATH, '/html/body/div[1]/form[1]/div/div/div[2]/div[1]/div/div/div/div/div/div[3]/div/div[2]/div/div[4]/div[1]/div/div/div/div[1]/a').click()

        time.sleep(5)

        email = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/div/div[1]/div[2]/div/div[1]/div/div/form/div/div[3]/div/div[1]/label/span').text

    except:
        pass
    driver.quit()
    return {
        "email": email
    }
