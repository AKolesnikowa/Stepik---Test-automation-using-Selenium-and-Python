from selenium import webdriver
import time 
from selenium.webdriver.support.ui import Select


link = "http://suninjuly.github.io/selects2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    a = browser.find_element_by_id('num1').text
    b = browser.find_element_by_id('num2').text

    x = str(int(a) + int(b))

    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(f"{x}")

    button = browser.find_element_by_css_selector("[type='submit']")
    button.click()

finally:
    # 
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла