import pickle
import selenium.webdriver 

driver = selenium.webdriver.Chrome('./chromedriver')

driver.get("https://sms-activate.ru/ru") 

cookies = pickle.load(open("cookies.pkl", "rb")) 
for cookie in cookies: 
    driver.add_cookie(cookie) 
