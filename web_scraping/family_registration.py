from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
import time
from functionalities.img_url_generator import img_url_generator


def family_registration(user_name, user_pass):

    url='https://eservices.cspd.gov.jo/index-rtl.html'
    driver = webdriver.Firefox()
    driver.get(url)

    wait = WebDriverWait(driver,50)

    user_name_input_field = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[name="username"]')))
    user_name_input_field.clear()
    user_name_input_field.send_keys(user_name)

    user_pass_input_field = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[name="password"]')))
    user_pass_input_field.clear()
    user_pass_input_field.send_keys(user_pass)

    login_button = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@type="submit"]')))
    login_button.click()

    button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[data-filter=".Certificates"]')))
    time.sleep(5)

    button.click()

    time.sleep(5)

    element_id="ServicesMenu_widget_ServicesMenu_0"
    element = wait.until(EC.visibility_of_element_located((By.ID, element_id)))
    child_elements = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "h4")))

    target_text = 'إصدار شهادة القيد العائلي'
    for i in child_elements :
        if (i.text == target_text):
            print('i is',i)
            print(i.text)
            parent_element = i.find_element(By.XPATH, '..')
            parent_html = parent_element.get_attribute('outerHTML')
            print(parent_html)
            parent_element.click()
            
        continue

    time.sleep(5)
    next_button= wait.until(EC.presence_of_element_located((By.CLASS_NAME, "btn.mx-button.mx-name-actionButton9.fa.Next.mobilebtn.btn-default")))
    time.sleep(5)
    next_button.click()

    time.sleep(2)

    rel_dropdown = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "mxui_widget_ReferenceSelector_1_input"))
    )
    # Select the first option in the dropdown
    select_first = Select(rel_dropdown)
    select_first.select_by_index(1)

    # Verify the selected option
    selected_option = select_first.first_selected_option
    selected_value = selected_option.get_attribute("value")

    time.sleep(5)

    reg_dropdown = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.ID, "mxui_widget_ReferenceSelector_2_input")))

    select_one =Select(reg_dropdown)
    select_one.select_by_index(1)

    selected_option = select_one.first_selected_option
    selected_value = selected_option.get_attribute("value")

    time.sleep(5)

    # Wait for the dropdown element to be present and visible
    dropdown_locator = (By.CSS_SELECTOR, "div.mx-name-dropDown3.required.langlist.mx-dropdown.form-group.no-columns")
    dropdown = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(dropdown_locator))
    dropdown.click()

    option_locator = (By.XPATH, "//option[contains(text(), 'عربي')]")
    option = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(option_locator))
    option.click()

    time.sleep(5)
    next_button= wait.until(EC.presence_of_element_located((By.CLASS_NAME, "btn.mx-button.mx-name-actionButton9.fa.Next.mobilebtn.btn-default")))
    time.sleep(5)
    next_button.click()

    dropdown_locator = (By.CSS_SELECTOR, "div.mx-name-dropDown1.mx-dropdown.form-group.no-columns")
    dropdown = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(dropdown_locator))
    dropdown.click()

    option_locator = (By.XPATH, "//option[contains(text(), 'إي فواتيركم')]")
    option = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(option_locator))
    option.click()

    dropdown_locator = (By.CSS_SELECTOR, "div.mx-name-dropDown2.required.mx-dropdown.form-group.no-columns")
    dropdown = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(dropdown_locator))
    dropdown.click()

    option_locator = (By.XPATH, "//option[contains(text(), 'مكاتب الأحوال المدنية و الجوازات')]")
    option = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(option_locator))
    option.click()

    review_dropdown = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "mxui_widget_ReferenceSelector_3_input"))
    )

    select_review = Select(review_dropdown)
    time.sleep(5)
    provided_text = "عمان الغربيه"

    for option in select_review.options:
        if provided_text in option.text:
            option.click()
            break
    time.sleep(5)

    ropdown_locator = (By.CSS_SELECTOR, "div.mx-name-dropDown5.required.mx-dropdown.form-group.no-columns")
    dropdown = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(dropdown_locator))
    dropdown.click()

    option_locator = (By.XPATH, "//option[contains(text(), 'إي فواتيركم الدفع المباشر')]")
    option = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(option_locator))
    option.click()

    element_locator = (By.CSS_SELECTOR, "div.widget-switch-btn-wrapper")
    element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(element_locator))

    # Check if the element is currently unchecked
    if "un-checked" in element.get_attribute("class"):
    # Click on the element to change its state to "checked"
        element.click()

    button_approval = (By.CSS_SELECTOR, "button.btn.btn-primary")
    button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(button_approval))
    button.click()

    time.sleep(5)
    finish_button= wait.until(EC.presence_of_element_located((By.CLASS_NAME, "btn.mx-button.mx-name-actionButton9.mobilebtn.btn-default")))
    time.sleep(5)
    finish_button.click()

    info_element = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="mxui_widget_HorizontalScrollContainer_1"]')))
    info_screenshot = info_element.screenshot_as_png
    with open('../images/family_info.png', 'wb') as file:
        file.write(info_screenshot)

    driver.quit()
    return img_url_generator("../images/family_info.png")
