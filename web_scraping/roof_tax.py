from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bidi.algorithm import get_display
from arabic_reshaper import reshape
import time
from functionalities.img_url_generator import img_url_generator



def roof_tax(id_, card_id):

    # Configure Firefox to run in headless mode
    # options = webdriver.FirefoxOptions()
    # options.add_argument("--headless")
    # driver = webdriver.Firefox(options=options)
    
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

    time.sleep(10)

    lookup_button = driver.find_element(By.LINK_TEXT, "ضريبة الأبنية والمسقفات")
    lookup_button.click()

    id_input_field = driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_txtNationalNo")
    id_input_field.clear()
    id_input_field.send_keys(id_)

    card_id_input_field = driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_ID_NO")
    card_id_input_field.clear()
    card_id_input_field.send_keys(card_id)

    search_button = driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_btnSearch")
    search_button.click()

    page_element = driver.find_element(By.ID, 'ctl00_ContentPlaceHolder1_get_real')
    page_screenshot = page_element.screenshot_as_png
    with open('../images/all_roofs.png', 'wb') as file:
        file.write(page_screenshot)

    details_button = driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_get_real_ctl02_lnkrealdetails")
    details_button.click()

    page2_element = driver.find_element(By.XPATH, '/html/body/form/table/tbody/tr[2]/td[2]/table/tbody/tr[7]/td/table/tbody/tr[1]/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td/table/tbody/tr[1]/td/table/tbody/tr[2]/td/table/tbody/tr[4]/td')
    page2_screenshot = page2_element.screenshot_as_png
    with open('../images/roof_tax_1.png', 'wb') as file:
        file.write(page2_screenshot)
    driver.quit()
    return img_url_generator("../images/all_roofs.png"), img_url_generator("../images/roof_tax_1.png")