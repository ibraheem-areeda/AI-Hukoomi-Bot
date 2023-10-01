from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bidi.algorithm import get_display
from arabic_reshaper import reshape
import time

# Configure Firefox to run in headless mode
# options = webdriver.FirefoxOptions()
# options.add_argument("--headless")
# driver = webdriver.Firefox(options=options)
def violations_lookup(keyword):
    driver = webdriver.Firefox()
    driver.get('https://www.amman.jo/ar/eservices/login.aspx')

    user_name = 9991015666
    user_pass = "Z=vNgg,;w5GNiRhd2f"

    user_name_input_field = driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_txtUserName")
    user_name_input_field.clear()
    user_name_input_field.send_keys(user_name)

    user_pass_input_field = driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_txtPassword")
    user_pass_input_field.clear()
    user_pass_input_field.send_keys(user_pass)

    sign_in_button = driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_cmdSubmit")
    sign_in_button.click()

    time.sleep(9)

    lookup_button = driver.find_element(By.LINK_TEXT, "قيم مخالفات السير")
    lookup_button.click()

    lookup_violations_text = keyword  # ***** USER INPUT ***** USER INPUT ***** USER INPUT ***** USER INPUT ***** USER INPUT ***** USER INPUT *****
    lookup_violations_text_box = driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_txtTicketDescription")
    lookup_violations_text_box.clear()
    lookup_violations_text_box.send_keys(lookup_violations_text)

    search_vehicle_button = driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_btnSearch")
    search_vehicle_button.click()

    violations_table_id = "ctl00_ContentPlaceHolder1_ytr"

    violation_rows = driver.find_elements(By.CLASS_NAME, "tableView")
    
    reshaped_text = reshape(violation_rows[0].text)
    
    driver.quit()
    lines = reshaped_text.splitlines()[3:]
    if len(lines) > 1:
        total_lines = len(lines)
        split_index = round(total_lines / 2)

        first_half = '\n'.join(lines[:split_index])
        second_half = '\n'.join(lines[split_index:])
        return first_half, second_half
    else:
        return lines[0]