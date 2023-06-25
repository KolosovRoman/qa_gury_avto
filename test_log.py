import time

from selene import browser, have

browser.config.driver_name = "firefox"

def test_login_qagury():
    browser.open("https://qa.guru/cms/system/login")
    browser.element(".login-form [name=email]").type("roman95kolos@gmail.com")
    browser.element(".login-form [name=password]").type("reo12reo").press_enter()

    time.sleep(5)
    browser.element(".main-header__login").click()
    browser.element(".logined-form").should(have.text("крео"))
    browser.should(have.url_containing("/cms/system/login"))

