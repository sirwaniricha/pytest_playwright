import requests
from playwright import sync_api

class Login:
    def __init__(self,data):
        self.user_name = data['username']
        self.password = data['password']
        self.env = data.get('env')

    def do_login(self, page: sync_api.Page):

        page.goto("https://www.saucedemo.com")
        page.locator("//*[@data-test='user-name']").fill(self.user_name)
        page.locator("//*[@data-test='password']").fill(self.password)
        page.locator('//*[@data-test="login-button"]').click()
        self.validate_login(page)

    def validate_login(self, page: sync_api.Page):
        try:
            sync_api.expect(page).to_have_title("Swag Labs")
        except:
            print("Login failed")


