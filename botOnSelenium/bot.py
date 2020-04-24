import time
from selenium import webdriver

def main():
    driver = webdriver.Chrome(executable_path="./chromedriver")
    driver.get('https://sms-activate.ru/ru/api_doc')
    reg_btn = driver.find_element_by_css_selector('a[data-target = ".bs-example-modal-lg"]')

    reg_btn.click()
    time.sleep(0.6)
    email_field = driver.find_element_by_css_selector('input.form-control[name="email"]')
    email_field.send_keys('grekovdima7@gmail.com')
    pass_field = driver.find_element_by_css_selector('')
    time.sleep(5)

if __name__ == '__main__':
    main()
