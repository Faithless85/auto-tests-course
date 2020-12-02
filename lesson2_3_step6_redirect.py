from selenium import webdriver
import time
import numpy as np

try:
    browser = webdriver.Opera()
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser.get(link)


    def calc(x):
        z = np.log(abs(12 * np.sin(x)))
        return z


    button1 = browser.find_element_by_tag_name("button").click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    
    x_element = browser.find_element_by_id('input_value')
    x = int(x_element.text)
    y = calc(x)

    input1 = browser.find_element_by_id("answer").send_keys(str(y))
    button = browser.find_element_by_tag_name("button").click()

finally:
    time.sleep(10)
    browser.quit()
