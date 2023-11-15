from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set up the Chrome WebDriver
driver = webdriver.Chrome()

# Navigate to the login page
driver.get("https://sso.teachable.com/secure/146684/identity/login/password")

try:
    # Replace with your actual login credentials
    email = "a.joseph.192@westcliff.edu"
    password = "$DMiS.qm&yY=Z3C"

    # Wait for the email input field to be present (you may need to adjust the timeout)
    email_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "login[email]"))
    )

    # Find the password input field
    password_input = driver.find_element(By.NAME, "login[password]")

    # Enter the credentials
    email_input.send_keys(email)
    password_input.send_keys(password)

    # Submit the login form
    password_input.send_keys(Keys.ENTER)

    # Wait for some time to ensure the login is complete (you may need to adjust this)
    time.sleep(5)

    # Navigate to the page with the videos
    driver.get("https://members.codewithmosh.com/courses/enrolled/240431")

except Exception as e:
    print(f"Error during login: {e}")
    driver.quit()
    exit(1)

# Wait for the page to load (you may need to adjust this)
time.sleep(5)

# Find and print the video links
video_links = []
for link in driver.find_elements(By.TAG_NAME, "a"):
    href = link.get_attribute("href")
    if href and href.endswith('.mp4'):
        video_links.append(href)

# Download the videos
for link in video_links:
    try:
        driver.get(link)

        # Wait for the video to load (you may need to adjust this)
        time.sleep(5)

        # Add code here to download the video
        # ...

    except Exception as e:
        print(f'Error downloading video {link}: {e}')

# Close the browser
driver.quit()
