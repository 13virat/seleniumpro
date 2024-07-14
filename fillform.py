from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

# Set the path to the chromedriver
chrome_driver_path = "/usr/local/bin/chromedriver"

# Create a service object
service = Service(chrome_driver_path)

# Create options object and add necessary options
chrome_options = Options()

# Initialize the WebDriver
driver = webdriver.Chrome(service=service, options=chrome_options)

# URL of the Google Form
url = "https://docs.google.com/forms/d/e/1FAIpQLSdUCd3UWQ3VOgeg0ZzNeT-xzNawU8AJ7Xidml-w1vhfBcvBWQ/viewform"

# Open the URL
driver.get(url)

def fill_form(fullname, contact, email, address, pincode, dob, gender, code):
    # Wait for the form elements to be present
    time.sleep(2)  # wait for the form to load

    # Find all input elements by class name
    inputs = driver.find_elements(By.CLASS_NAME, "whsOnd")

    # List of input values
    inputs_array = [fullname, contact, email, pincode, dob, gender, code]

    for i in range(len(inputs_array)):
        # Clear the input field
        inputs[i].clear()
        # Enter the data into the input field
        inputs[i].send_keys(inputs_array[i])

    # Find the textarea element by class name
    address_input = driver.find_element(By.CLASS_NAME, "KHxj8b")
    # Clear the textarea field
    address_input.clear()
    # Enter the data into the textarea field
    address_input.send_keys(address)

    # Optionally, you may want to submit the form
    submit_button = driver.find_element(By.CLASS_NAME, "NPEfkd")
    submit_button.click()
    #Take a screenshot before submitting the form
    driver.save_screenshot('form_filled.png')

# Fill the form with the provided data
fill_form("virat gupta", "3456789987", "virat@gmail.com", 'house A', '12345', "12/12/2012", "Male", "GNFPYC")

# Add a delay to keep the browser open
time.sleep(10)

# Close the browser
driver.quit()
