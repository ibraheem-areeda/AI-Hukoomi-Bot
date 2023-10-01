from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from functionalities.img_url_generator import img_url_generator


def to_whom_it_may_concern(user_name, user_pass):
    driver = webdriver.Firefox()
    driver.get('https://eservices.ssc.gov.jo/external/login')

    # ***** USER INPUT ***** USER INPUT ***** USER INPUT ***** USER INPUT ***** USER INPUT ***** USER INPUT *****
    user_name = user_name
    user_pass = user_pass
    # user_name = 9931031969
    # user_pass = "1@Jan1993"
    # ***** USER INPUT ***** USER INPUT ***** USER INPUT ***** USER INPUT ***** USER INPUT ***** USER INPUT *****

    user_name_input_field = driver.find_element(By.ID, "mat-input-0")
    user_name_input_field.clear()
    user_name_input_field.send_keys(user_name)

    user_pass_input_field = driver.find_element(By.ID, "mat-input-1")
    user_pass_input_field.clear()
    user_pass_input_field.send_keys(user_pass)

    sign_in_button = driver.find_element(By.CLASS_NAME, "btn-success")
    sign_in_button.click()

    time.sleep(3)

    whom_it_concern_button = driver.find_element(By.ID, "mat-expansion-panel-header-8")
    driver.execute_script("arguments[0].scrollIntoView(true);", whom_it_concern_button)
    whom_it_concern_button.click()

    time.sleep(4)

    driver.switch_to.window(driver.window_handles[-1])

    dropdown_menu = driver.find_element(By.XPATH, '//*[@id="scaleSelect"]')
    dropdown_menu.click()

    option = driver.find_element(By.XPATH, '//*[@id="pageFitOption"]')
    option.click()

    page_element = driver.find_element(By.CSS_SELECTOR, '.textLayer')
    page_screenshot = page_element.screenshot_as_png
    with open('../images/to_whom_it_may_concern.png', 'wb') as file:
        file.write(page_screenshot)

    driver.quit()
    return img_url_generator("../images/to_whom_it_may_concern.png")

