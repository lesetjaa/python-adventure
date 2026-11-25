from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import NoSuchElementException, TimeoutException
import os
from time import sleep
from dotenv import load_dotenv

load_dotenv()
# ---------------------- STEP 1: Setup Chrome Profile and Webdriver ----------------------


URL = "https://appbrewery.github.io/gym/"
ACCOUNT_EMAIL = os.environ["ACCOUNT_EMAIL"]
ACCOUNT_PASSWORD = os.environ["ACCOUNT_PASSWORD"]


def retry(func, retries=7, description=None):
    for i in range(retries):
        print(f"Trying {description}. Attempt: {i + 1}")
        try:
            return func()
        except TimeoutException:
            if i == retries - 1:
                raise
            sleep(1)


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

user_data_dir = os.path.join(os.getcwd(), "chrome_profile")
chrome_options.add_argument(f"--user-data-dir={user_data_dir}")

driver = webdriver.Chrome(options=chrome_options)
wait = WebDriverWait(driver, 2)

driver.get(url=URL)

# ---------------------- STEP 2: Automated Login ----------------------


def login():
    login_btn = wait.until(EC.element_to_be_clickable((By.ID, "login-button")))
    login_btn.click()

    fill_email = wait.until(
        EC.presence_of_element_located((By.ID, "email-input")))
    fill_email.clear()
    fill_email.send_keys(ACCOUNT_EMAIL)

    fill_password = driver.find_element(By.ID, "password-input")
    fill_password.clear()
    fill_password.send_keys(ACCOUNT_PASSWORD)

    submit_btn = driver.find_element(By.ID, "submit-button")
    submit_btn.click()

    wait.until(EC.presence_of_element_located((By.ID, "schedule-page")))
    print("✓ Logged In")


def book_class(book_btn):
    book_btn.click()
    wait.until(lambda d: book_btn.text == "Booked")


retry(func=login, description="login")

class_cards = driver.find_elements(By.CSS_SELECTOR, 'div[id^="class-card-"]')
booked_count = 0
waitlist_count = 0
already_booked_count = 0
booking_list = []

for card in class_cards:
    # Look for tuesday in the parent of the class
    day_group = card.find_element(
        By.XPATH, "./ancestor::div[contains(@id, 'day-group-')]")
    day_title = day_group.find_element(By.TAG_NAME, "h2").text  # Find title

    if "Tue" in day_title or "Thu" in day_title:
        time_text = card.find_element(
            By.CSS_SELECTOR, "p[id^='class-time-']").text

        if "6:00 PM" in time_text:
            class_name = card.find_element(By.TAG_NAME, "h3").text
            book_btn = card.find_element(
                By.CSS_SELECTOR, 'button[id^="book-button-"]')
            class_details = f"{class_name} on {day_title}"

            if book_btn.text == "Booked":
                already_booked_count += 1
                print(f"✓ Already booked: {class_details}")

            elif book_btn.text == "Waitlisted":
                already_booked_count += 1
                print(f"✓ Already on waitlist: {class_details}")

            elif book_btn.text == "Join Waitlist":
                retry(lambda: book_class(book_btn), description="booking class")
                print(f"✓ Joined waitlist for: {class_details}")
                booking_list.append(f"[New Waitlist] {class_details}")
                waitlist_count += 1
                sleep(0.5)

            else:
                retry(lambda: book_class(book_btn), description="booking class")
                print(f"✓ Successfully Booked: {class_details}")
                booking_list.append(f"[New Booking] {class_details}")
                booked_count += 1
                sleep(0.5)
            


total_booked = booked_count + waitlist_count + already_booked_count
print(f"\n--- Total Tuesday/Thursday 6pm classes: {total_booked} ---")
print("\n--- VERIFYING ON MY BOOKINGS PAGE ---")

# Print summary
print("\n--- BOOKING SUMMARY ---")
print(f"Classes booked: {booked_count}")
print(f"Waitlists joined: {waitlist_count}")
print(f"Already booked/waitlisted: {already_booked_count}")
print(f"Total Tuesday 6pm classes processed: {total_booked}")

print("\n--- DETAILED CLASS LIST ---")
for new_booking in booking_list:
    print("  • " + new_booking, end="\n")


def get_my_bookings():
    global verified_count

    my_bookings_nav = driver.find_element(By.CSS_SELECTOR, "#my-bookings-link")
    my_bookings_nav.click()
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "h1")))

    my_booked_classes = driver.find_elements(
        By.CSS_SELECTOR, 'div[id^="booking-card-"]')
    my_booked_classes.extend(driver.find_elements(
        By.CSS_SELECTOR, 'div[id^="waitlist-card-"]'))

    if not my_booked_classes:
        raise TimeoutException

    return my_booked_classes


all_cards = retry(get_my_bookings, description="get bookings")

verified_count = 0

for booked_class in all_cards: # type: ignore
    try:
        class_date = booked_class.find_element(
            By.CSS_SELECTOR, "p:first-of-type").text

        if ("Tue" in class_date or "Thu" in class_date) and "6:00 PM" in class_date:
            verified_count += 1
            class_title = booked_class.find_element(By.TAG_NAME, "h3").text
            print(f"  ✓ Verified: {class_title}")
    except NoSuchElementException:
        pass


retry(func=get_my_bookings, description="get bookings")


print("\n--- VERIFICATION RESULT ---")
print(f"Expected: {total_booked} bookings")
print(f"Found: {verified_count} bookings")
print(f"✅ SUCCESS: All bookings verified!" if total_booked ==
      verified_count else f"❌ MISMATCH: Missing {total_booked - verified_count} bookings")


driver.quit()
