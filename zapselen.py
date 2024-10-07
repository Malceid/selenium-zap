from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

# Set up Chrome options with the OWASP ZAP proxy (if needed, otherwise leave as is)
chrome_options = Options()
# Example of proxy settings if necessary
chrome_options.add_argument('--proxy-server=http://127.0.0.1:8081') #Change to 8080 if your port in ZAP is also 8080

# Initialize the WebDriver with Chrome options
driver = webdriver.Chrome(options=chrome_options)

try:
    # Open the target webpage
    driver.get('https://main-dwt.store/')  # Maybe a phishing link? Edit the links here

    # Wait for the page to load
    time.sleep(2)

    # Try finding the email input field
    email_found = False
    try:
        email_input = driver.find_element(By.NAME, 'email')  # Try to find the email field
        email_input.send_keys('testuser@example.com')  # Use a test email
        email_found = True
    except Exception as e:
        print("Email input not found, skipping.")

    # Try finding the username input field
    username_found = False
    try:
        username_input = driver.find_element(By.NAME, 'username')  # Try to find the username field
        username_input.send_keys('tomsmith')  # Use a test username
        username_found = True
    except Exception as e:
        print("Username input not found, skipping.")

    # Find the password input field
    try:
        password_input = driver.find_element(By.NAME, 'password')
        password_input.send_keys('SuperSecretPassword!')
    except Exception as e:
        print("Password input not found.")

    # Submit the form (assuming password field or form supports Enter key to submit)
    try:
        password_input.send_keys(Keys.RETURN)
        time.sleep(2)  # Wait for the form submission process
    except Exception as e:
        print("Error in submitting the form.")

    # Debugging: Check the current URL after submission
    print("Current URL after submission:", driver.current_url)

    # Optionally, check if the <h1> element exists on the resulting page
    try:
        response_message = driver.find_element(By.TAG_NAME, 'h1').text
        print("Response message:", response_message)
    except Exception as e:
        print("No <h1> element found on the response page, but continuing.")

    # Find and print all URLs on the current page
    print("Extracting all URLs from the page...")
    links = driver.find_elements(By.TAG_NAME, 'a')  # Locate all <a> elements
    for link in links:
        url = link.get_attribute('href')  # Extract the URL from the href attribute
        if url:
            print(url)

finally:
    # Close the driver after the test
    driver.quit()