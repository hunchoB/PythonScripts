from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait



# Read user data into array from the file
authentification = []
file = open('C:/Users/a.bobkov/Desktop/aut_data.txt', 'r')

for line in file:
    words = line.split(',')
    authentification += words

file.close()

browser = webdriver.Chrome("D:/vscodeProjects/Python/chromedriver.exe")
browser.get("https://account.habr.com/login/?state=a3031641b2a8fe6fca87b9a3d6b5e7d7&consumer=habr&hl=ru_RU")



# login_input = browser.find_element_by_id('email_field')
# login_input.send_keys(authentification[0])

# password_input = browser.find_element_by_id('password_field')
# password_input.send_keys(authentification[1])
WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, "email_field")))
confirm_button = browser.find_element_by_name('go').click()

# browser.refresh()