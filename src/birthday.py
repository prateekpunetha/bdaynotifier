#!/usr/bin/env python3
from playwright.sync_api import  sync_playwright
import toml

config = toml.load('../config.toml')

username = config['credentials']['username']
password = config['credentials']['password']
chatid = config['credentials']['chatid']
base_url = config['credentials']['base_url']

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto(base_url)

    page.type("input.form-control", username)
    page.type("#passwordValue", password)
    page.click(".submit-login")
    page.wait_for_timeout(8000)

    page.goto("https://portal.vmedulife.com/student/Summary.php")

    divContent = page.inner_html(".scroll-card-birthday")

    browser.close()
