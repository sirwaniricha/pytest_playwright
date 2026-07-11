import requests
from playwright import sync_api

class Login:


    def do_login(self, page: sync_api.Page,data):
        page.goto("https://www.saucedemo.com")
        page.locator("//*[@data-test='user-name']").fill(data["username"])
        page.locator("//*[@data-test='password']").fill(data["password"])
        page.locator('//*[@data-test="login-button"]').click()
        if "expected_error_message" not in data:
            self.validate_login(page)
        else:
            self.validate_negative_login(page, data["expected_error_message"])

    def validate_login(self, page: sync_api.Page):
        try:
            sync_api.expect(page).to_have_title("Swag Labs")
        except:
            print("Login failed")
        else:
            print("Login successful")

    def validate_negative_login(self, page: sync_api.Page, message: str):
        print("validating login : negative case")
