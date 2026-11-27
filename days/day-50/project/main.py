from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException, TimeoutException
from dotenv import load_dotenv
from time import sleep
import os

load_dotenv()

FACEBARK_EMAIL = os.environ["FACEBARK_EMAIL"]
FACEBARK_PASSWORD = os.environ["FACEBARK_PASSWORD"]
TINDOG_URL="https://app.100daysofpython.dev/services/tindog/u/WqiJ0BNf9_0F0yR5AOGbW4Ak5qU-7wR4"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

wait = WebDriverWait(driver, 5)
driver.get(url=TINDOG_URL)


# Login
wait.until(EC.presence_of_element_located((By.CLASS_NAME, "tindog-brand")))
login_btn = driver.find_element(By.CLASS_NAME, "btn-tindog-login")
login_btn.click()

sleep(2)
facebark_btn = driver.find_element(By.CLASS_NAME, "btn-facebark")
facebark_btn.click()

# Facebrak pop up
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)

sleep(2)
email_input = driver.find_element(By.NAME, "email")
email_input.clear()
email_input.send_keys(FACEBARK_EMAIL)


password_input = driver.find_element(By.NAME, "pass")
password_input.clear()
password_input.send_keys(FACEBARK_PASSWORD)

submit_btn = driver.find_element(By.XPATH, "/html/body/div[2]/div/form/button")
submit_btn.click()

driver.switch_to.window(base_window)

# dismiss requests
sleep(1)
allow_btn = driver.find_element(By.CLASS_NAME, "btn-primary")
allow_btn.click()

sleep(1)
enable_location_btn = driver.find_element(By.XPATH, '//button[text()="Not interested"]')
enable_location_btn.click()

sleep(1)
accept_cookies_btn = driver.find_element(By.CSS_SELECTOR, "button.btn-primary")
accept_cookies_btn.click()

# Swiping Right!
liked_count = 20
while liked_count > 0:
    sleep(1.5)
    try:
        like_btn = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "btn-like")))
        like_btn.click()
        liked_count -= 1
    except ElementClickInterceptedException: # Its a match pop up
        try:
            back_btn = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "match-popup-link")))
            back_btn.click()
        except NoSuchElementException:
            sleep(2) 
    except NoSuchElementException:
        sleep(2)
    print(liked_count)

driver.quit()

