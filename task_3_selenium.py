from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

import time


def yandex_auth():
    chrome_path = ChromeDriverManager().install()
    browser_service = Service(executable_path=chrome_path)
    o = Options()
    o.add_experimental_option("detach", True)
    browser = Chrome(service=browser_service, options=o)

    browser.get('https://passport.yandex.ru/auth/')
    login = browser.find_element(by=By.ID, value='passp-field-login')
    login.click()
    login.send_keys('avtorus.serwis')
    browser.find_element(by=By.ID, value='passp:sign-in').click()
    time.sleep(1)

    try:
        login_err = browser.find_element(by=By.ID, value='field:input-login:hint')
        return login_err.text.strip()
    except:
        print('Логин введел')

    passw = browser.find_element(by=By.ID, value='passp-field-passwd')
    passw.click()
    passw.send_keys('214365qwe!')
    browser.find_element(by=By.ID, value='passp:sign-in').click()
    time.sleep(1)

    try:
        passw_err = browser.find_element(by=By.ID, value='field:input-passwd:hint')
        return passw_err.text.strip()
    except:
        print('Пароль введен')

    result = browser.current_url
    browser.close()
    return result


    
print(yandex_auth())

