from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(options=options)

# url = 'https://google.com'
# url = 'http://127.0.0.1:5500/Test.html'
url = 'https://znit.netlify.app/'
driver.get(url)

# driver.find_element_by_css_selector('.selectfile').click()
# driver.find_element_by_css_selector("input[type='file']")

# driver.find_element_by_css_selector('.gb_1').click() // 구글 로그인 테스트용

driver.find_element_by_css_selector(".selectfile").send_keys(r"C:\Users\jiheon\Desktop\znit\url_list_result.txt")
# driver.find_element_by_css_selector('.selectfile').send_keys(Keys.ENTER)
