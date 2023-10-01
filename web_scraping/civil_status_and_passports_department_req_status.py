from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from functionalities.img_url_generator import img_url_generator


def civil_status_and_passports_department_req_status(user_name, user_pass):
    url='https://eservices.cspd.gov.jo/index-rtl.html'
    driver = webdriver.Firefox()
    driver.get(url)
    driver.maximize_window()
    wait = WebDriverWait(driver,50)

    user_name = user_name
    user_pass = user_pass
    # user_name = 9912017766
    # user_pass = "luluRe*91"
    
    user_name_input_field = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[name="username"]')))
    user_name_input_field.clear()
    user_name_input_field.send_keys(user_name)

    user_pass_input_field =wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[name="password"]')))  # Replace with the actual name attribute of the password field
    user_pass_input_field.clear()
    user_pass_input_field.send_keys(user_pass)

    login_button = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@type="submit"]')))
    login_button.click()

    time.sleep(12)

    option = driver.find_element(By.CSS_SELECTOR, '.mx-name-container22')
    option.click()

    time.sleep(7)
                
    page_element = driver.find_element(By.CSS_SELECTOR, '.mx-groupbox-body')

    page_screenshot = page_element.screenshot_as_png
    with open('../images/civil_status_and_passports_department_req_status.png', 'wb') as file:
        file.write(page_screenshot)
    driver.quit()
    return img_url_generator("../images/civil_status_and_passports_department_req_status.png")
