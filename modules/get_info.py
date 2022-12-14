import contextlib
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

    with contextlib.suppress(Exception):
        driver.find_element(By.XPATH,
                                  '/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[2]/div/div[1]/div/div/button').click()

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[2]/div/div[2]/div/div/button"))
        )

        time.sleep(5)

        model = click_result(driver, '/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[2]/div/div[2]/div/div/button', '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/section/header/div/h2/span')

        tel = click_result(driver, '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div[2]/div[2]/div/div/button', '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/span/span')

        phone = tel

    driver.quit()
    return {
        "model": model,
        "phone": phone
    }


def click_result(driver, xpath1, xpath2):
    """click_result: it clicks on the first result and returns the text of the second result

    Args:
        driver (driver): driver of the browser
        xpath1 (str): xpath of the first result
        xpath2 (str): xpath of the second result

    Returns:
        str: text of the second result
    """    
    driver.find_element(By.XPATH, xpath1).click()

    time.sleep(5)

    return driver.find_element(By.XPATH, xpath2).text


def yahoo(username):
    global phone
    phone = None
    options = uc.ChromeOptions()
    driver = uc.Chrome(options=options)

    driver.get("https://login.yahoo.com/")

    with contextlib.suppress(Exception):
        phone = yahoo_phone(driver, username)
    driver.quit()
    return {
        "phone": phone
    }


def yahoo_phone(driver, username):
    """yahoo_phone: it returns the phone number of the user

    Args:
        driver (driver): driver of the browser
        username (str): username of the user

    Returns:
        str: phone number of the user
    """    
    driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div[2]/div[2]/form/div[1]/div[3]/input').send_keys(username)

    time.sleep(0.5)

    driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div[2]/div[2]/form/div[2]').click()

    time.sleep(0.5)

    driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div[2]/div[2]/form/div[4]/input').click()

    time.sleep(5)

    return driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div[2]/div[2]/form/ul/li[2]').get_attribute("data-display")


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

    except Exception:
        pass
    driver.quit()
    return {
        "email": email
    }
