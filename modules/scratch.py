from selenium import webdriver
from selenium.webdriver.common.by import By


def scratch(username):
    global group, location, about, about2, friends
    group = None
    location = None
    about = None
    about2 = None
    friends = None

    driver = webdriver.Chrome(executable_path="/Driver/chromedriver.exe")

    driver.get(f"https://scratch.mit.edu/users/{username}/")

    try:
        try:
            group = driver.find_element(By.XPATH, '/html/body/div[1]/div[4]/div[2]/div[1]/div/p/span[1]').text
        except:
            pass
        try:
            location = driver.find_element(By.CLASS_NAME, 'location').text
        except:
            pass
        try:
            about = driver.find_element(By.XPATH, '/html/body/div[1]/div[4]/div[2]/div[2]/div[2]/div[1]/div[1]/div[2]/div/p').text
        except:
            pass
        try:
            about2 = driver.find_element(By.XPATH, '/html/body/div[1]/div[4]/div[2]/div[2]/div[2]/div[1]/div[1]/div[3]/div/p').text
        except:
            pass

        driver.get(f"https://scratch.mit.edu/users/{username}/following")

        i = 1
        friends = []

        while True:
            i += 1
            try:
                friend = driver.find_element(By.XPATH, f'/html/body/div[1]/div[4]/div[2]/div[2]/div/ul/li[{i}]')
                friends.append(friend)
            except:
                break
            i += 1

    except:
        print("User not found")
    driver.quit()

    return {
        "group": group,
        "location": location,
        "about": about,
        "about2": about2,
        "friends": friends
    }
