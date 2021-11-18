from selenium import webdriver
import time 

#вычисляем х:
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/redirect_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    butt_1 = browser.find_element_by_css_selector("[type='submit']")
    butt_1.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    x_element = browser.find_element_by_id('input_value')
    x = x_element.text
    y = calc(x)

    input_x = browser.find_element_by_id('answer')
    input_x.send_keys(y)
    
    butt_2 = browser.find_element_by_css_selector("[type='submit']")
    butt_2.click()


finally:
    # 
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()