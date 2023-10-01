from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from functionalities.img_url_generator import img_url_generator


def vehicle_validation(license_plate, license_plate_id, registration_num):

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

    element_id = "table1"
    wait = WebDriverWait(driver, 10)
    element = wait.until(EC.visibility_of_element_located((By.ID, element_id)))

    # driver.implicitly_wait(30)
    driver.get('https://www.amman.jo/ar/eservices/TicketQueryCS.aspx')
    license_plate = license_plate
    license_plate_input_field = driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_txtLicenseNo")
    license_plate_input_field.clear()
    license_plate_input_field.send_keys(license_plate)

    license_plate_id = license_plate_id
    license_plate_id_input_field = driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_txtNo")
    license_plate_id_input_field.clear()
    license_plate_id_input_field.send_keys(license_plate_id)

    registration_num = registration_num
    registration_num_input_field = driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_txtregNo")
    registration_num_input_field.clear()
    registration_num_input_field.send_keys(registration_num)

    search_vehicle_button = driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_btnSearch")
    search_vehicle_button.click()

    page_element = driver.find_element(By.CSS_SELECTOR, '#ctl00_ContentPlaceHolder1_ytr > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(9) > td:nth-child(1) > table:nth-child(1)')
    page_screenshot = page_element.screenshot_as_png
    with open('../images/vehcile_violations.png', 'wb') as file:
        file.write(page_screenshot)

    driver.quit()
    return img_url_generator("../images/vehcile_violations.png")