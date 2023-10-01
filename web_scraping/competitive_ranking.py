
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from bidi.algorithm import get_display
from arabic_reshaper import reshape
from functionalities.img_url_generator import img_url_generator


def competitive_ranking(user_nat_no, persone_card_no):
    url = 'http://enq-sys.csb.gov.jo/'
    driver = webdriver.Firefox()
    driver.get(url)

    wait = WebDriverWait(driver, 10)

    user_nat_no_input_field = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[name="ctl00$ContentPlaceHolder1$txt_natno"]')))
    user_nat_no_input_field.clear()
    user_nat_no_input_field.send_keys(user_nat_no)

    user_persone_card_no_input_field = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[name="ctl00$ContentPlaceHolder1$txt_name"]')))
    user_persone_card_no_input_field.clear()
    user_persone_card_no_input_field.send_keys(persone_card_no)

    login_button = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@type="submit"]')))
    login_button.click()
    time.sleep(5)
    
    try :
        info_element = driver.find_element(By.XPATH, '//*[@id="ContentPlaceHolder1_EmploymentData1_GridCOMP_DXMainTable"]')
        info_screenshot = info_element.screenshot_as_png
        with open('../images/competitive_ranking.png', 'wb') as file:
            file.write(info_screenshot)
     
    except :  
        error_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="ContentPlaceHolder1_Error_Messg"]')))
        error_text = error_element.text
        reshaped_error_text = reshape(error_text)
        display_error_text = get_display(reshaped_error_text)
        print(display_error_text)

    driver.quit()

    return img_url_generator("../images/competitive_ranking.png")


