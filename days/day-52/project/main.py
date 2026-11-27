import os
from time import sleep
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException, TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin

load_dotenv()

SIMILAR_ACCOUNT = "chefsteps"
USERNAME = os.environ["SHARE_A_NAAN_USERNAME"]
PASSWORD = os.environ["SHARE_A_NAAN_PASSWORD"]
BASE_URL = "https://app.100daysofpython.dev/services/share-a-naan"
LOGIN_URL = f"{BASE_URL}/login"


class InstaFollower:
    def __init__(self) -> None:
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)  # keep the web browser open
        self.driver = webdriver.Chrome(options=chrome_options)
        self.wait = WebDriverWait(self.driver, 2)

    def login(self):
        # Login website
        self.driver.get(LOGIN_URL)
        self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "naan-brand")))

        username_input = self.driver.find_element(By.NAME, "username")
        username_input.clear()
        username_input.send_keys(USERNAME)

        password_input = self.driver.find_element(By.NAME, "password")
        password_input.clear()
        password_input.send_keys(PASSWORD)

        sleep(2)
        submit_btn = self.driver.find_element(By.CLASS_NAME, "naan-btn-primary")
        submit_btn.click()


        # Dismiss requests
        self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "naan-app")))
        dismiss_btn = self.driver.find_element(By.CLASS_NAME, "naan-popup-dismiss")
        dismiss_btn.click()

        sleep(1)
        dismiss_btn = self.driver.find_element(By.XPATH, '//button[contains(text(), "Not Now")]')
        dismiss_btn.click()

    def find_followers(self):
        sleep(1)
        self.driver.get(f"{BASE_URL}/u/{SIMILAR_ACCOUNT}")
        self.wait.until(EC.presence_of_element_located((By.XPATH, '//h1[contains(text(), "chefsteps")]')))
        followers = self.driver.find_element(By.CLASS_NAME, "naan-followers-link")
        followers.click()

        sleep(2)
        modal = self.driver.find_element(By.CSS_SELECTOR, ".followers-scroll")
        for _ in range(10):
            # "scroll this element to the bottom" → loads the next batch of followers
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            sleep(1)

    def follow(self):
        follow_btns = self.driver.find_elements(By.XPATH, "/html/body/div[2]/div/div[3]/div/button")
        for btn in follow_btns:
            try:
                btn.click()
            except ElementClickInterceptedException:
                try:
                    cancel_unfolow_btn = self.driver.find_element(By.CLASS_NAME, "naan-unfollow-cancel")
                    cancel_unfolow_btn.click()
                except NoSuchElementException:
                    sleep(2)
            sleep(1)
        print(f"Followed: {len(follow_btns)} users from {SIMILAR_ACCOUNT}'s account")

        self.driver.quit()


bot = InstaFollower()
bot.login()
bot.find_followers()
bot.follow()







