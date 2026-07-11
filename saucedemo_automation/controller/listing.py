from playwright.sync_api import expect, Page
from saucedemo_automation.utilities.components import ComponentsAutomation
class Listing(Page):
    def __init__(self,page:Page):
        self.components = ComponentsAutomation()

    def perform_actions_on_listing(self,test_data):
        print(test_data)

    def select_sorting(self,sort_by,page: Page):
        self.components.single_select_dropdown(page,"product-sort-container",sort_by)

    def click_on_cart(self,page: Page):
        page.locator("//*[@data-test='shopping-cart-link']").click()
        expect(page.get_by_title("Your Cart")).to_be_visible()
