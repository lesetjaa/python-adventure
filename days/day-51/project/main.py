from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import os
from dotenv import load_dotenv

load_dotenv()

PROMISED_DOWN = 150
PROMISED_UP = 10
Y_EMAIL = os.environ["Y_EMAIL"]
Y_PASSWORD = os.environ["Y_PASSWORD"]


class InternetSpeedTwitterBot:
    def __init__(self) -> None:
        self.down = 0
        self.up = 0
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)
        self.wait = WebDriverWait(self.driver, 3)

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")

        sleep(3.5)
        pop_up_btn = self.driver.find_element(By.ID, "onetrust-accept-btn-handler")
        pop_up_btn.click()

        sleep(1)
        test_speed_btn = self.driver.find_element(By.CSS_SELECTOR, "button[aria-label^='start speed']")
        test_speed_btn.click()

        sleep(60)
        speeds = [speed.text for speed in self.driver.find_elements(By.CSS_SELECTOR, '.MuiBox-root .css-0 h3')]
        self.down = float(speeds[0])
        self.up = float(speeds[1])

        print(f"down: {self.down}")
        print(f"up: {self.up}")

    def tweet_at_provider(self):
        self.driver.get("https://app.100daysofpython.dev/services/y")
        self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'y-logo-mark')))

        login_btn = self.driver.find_element(By.CSS_SELECTOR, "a.y-login-link")
        login_btn.click()

        sleep(1)
        email_input = self.driver.find_element(By.NAME, "email")
        email_input.clear()
        email_input.send_keys(Y_EMAIL)


        password_input = self.driver.find_element(By.NAME, "password")
        password_input.clear()
        password_input.send_keys(Y_PASSWORD)

        continue_btn = self.driver.find_element(By.CLASS_NAME, "y-login-submit")
        continue_btn.click()

        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "h1.x-header-title")))
        message = f"Hey Internet Provider, why is my speed {self.down}down/{self.up}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?!"
        post_input = self.driver.find_element(By.ID, "tweet-compose")
        post_input.send_keys(message)

        sleep(2)
        post_btn = self.driver.find_element(By.ID, "post-btn")
        post_btn.click()

        sleep(2)
        self.driver.quit()


bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.tweet_at_provider()