from selenium import webdriver

options = webdriver.ChromeOptions()
browser = webdriver.Chrome(options=options)
browser.maximize_window()

url = "https://mail.naver.com/"
