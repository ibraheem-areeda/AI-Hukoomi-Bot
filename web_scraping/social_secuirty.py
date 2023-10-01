from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from functionalities.img_url_generator import img_url_generator


def social_security(user_name, user_pass):

    # Configure Firefox to run in headless mode
    # options = webdriver.FirefoxOptions()
    # # options.add_argument("--headless")
    # driver = webdriver.Firefox(options=options)

    driver = webdriver.Firefox()
    driver.get('https://eservices.ssc.gov.jo/external/login')

    user_name = user_name # ***** USER INPUT ***** USER INPUT ***** USER INPUT ***** USER INPUT ***** USER INPUT ***** USER INPUT *****
    user_pass = user_pass # ***** USER INPUT ***** USER INPUT ***** USER INPUT ***** USER INPUT ***** USER INPUT ***** USER INPUT *****

    user_name_input_field = driver.find_element(By.ID, "mat-input-0")
    user_name_input_field.clear()
    user_name_input_field.send_keys(user_name)

    user_pass_input_field = driver.find_element(By.ID, "mat-input-1")
    user_pass_input_field.clear()
    user_pass_input_field.send_keys(user_pass)

    sign_in_button = driver.find_element(By.CLASS_NAME, "btn-success")
    sign_in_button.click()

    time.sleep(2)

    my_info_button = driver.find_element(By.ID, "mat-expansion-panel-header-0")
    my_info_button.click()

    time.sleep(2)

    lookup_button = driver.find_element(By.LINK_TEXT, "لوحة معلوماتي")
    lookup_button.click()

    time.sleep(10)

    close_popup_button = driver.find_element(By.ID, "searchat-chatbot-close-icon")
    close_popup_button.click()

    chart_element = driver.find_element(By.ID,'chart')
    chart_screenshot = chart_element.screenshot_as_png
    with open('../images/social_security_chart.png', 'wb') as file:
        file.write(chart_screenshot)

    info_element = driver.find_element(By.XPATH, '/html/body/app-root/app-layout-ssc/mat-sidenav-container/mat-sidenav-content/div/div/div/app-infoboard/mat-card/div[1]/div/div[2]/div')
    info_screenshot = info_element.screenshot_as_png
    with open('../images/social_security_info.png', 'wb') as file:
        file.write(info_screenshot)

    driver.quit()

    return img_url_generator("../images/social_security_info.png"), img_url_generator("../images/social_security_chart.png") 
