from playwright.sync_api import Page,expect

class ComponentsAutomation():

    def single_select_dropdown(self,page:Page, identifier, selection):
        page.locator("//*[@data-test='{}']".format(identifier)).click()
        page.get_by_text(selection).click()
        expect(page.locator("//*[@data-test='{}']".format(identifier))).to_have_text(selection)
