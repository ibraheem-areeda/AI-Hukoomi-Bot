from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from time import sleep
from functionalities.img_url_generator import img_url_generator

def land_location(land_key):

    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://maps.dls.gov.jo/dlsweb/index.html")
    select_element = Select(driver.find_element(By.ID, "form-search-select"))
    select_element.select_by_value("search_dlskey")
    ard = driver.find_element(By.ID, "txt_dlskey_search")
    ard.send_keys(land_key)
    ard_key = driver.find_element(By.ID, "dlskey_search-button")
    driver.implicitly_wait(10)
    ard_key.click()
    driver.implicitly_wait(30)
    sleep(10)
    driver.save_screenshot("../images/land_location.png")
    driver.quit()

    return img_url_generator("../images/land_location.png")
    

