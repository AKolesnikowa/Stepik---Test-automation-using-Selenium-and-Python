from selenium import webdriver
import time 

#вычисляем х:
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/math.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element_by_id('input_value')
    x = x_element.text
    y = calc(x)

    input_x = browser.find_element_by_id('answer')
    input_x.send_keys(y)

    #клик, чтобы поставить галочку или выбрать опцию
    chekbox1 = browser.find_element_by_id('robotCheckbox')
    chekbox1.click()
    radiobot = browser.find_element_by_id("robotsRule")
    radiobot.click()

    button = browser.find_element_by_css_selector("[type='submit']")
    button.click()


finally:
    # 
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла



