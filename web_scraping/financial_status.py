from selenium import webdriver
from arabic_reshaper import reshape
from selenium.webdriver.common.by import By

def financial_status(user_id):
    driver = webdriver.Firefox()
    driver.get('http://193.188.65.134:7777/')

    user_id = user_id                                     # الرقم الوطني

    input_field = driver.find_element(By.ID, "queryTextBox")
    input_field.clear()
    input_field.send_keys(user_id)

    button = driver.find_element(By.ID, "ImageButton1")
    button.click()

    response_element = driver.find_element(By.ID, "resultLabel")
    response_text = response_element.text
    reshaped_text = reshape(response_text)
    # display_text = get_display(reshaped_text)
    print(reshaped_text)

    driver.quit()
    return reshaped_text