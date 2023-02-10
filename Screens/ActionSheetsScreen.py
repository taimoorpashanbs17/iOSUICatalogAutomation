from Screens.BasePage import BasePage


class ActionSheetsScreen(BasePage):

    def __int__(self, driver):
        super().__init__(driver)

    def action_sheets_header_text(self):
        return self.get_text('ACTION_SHEETS_HEADER_NAME')

    def check_header_displaying(self):
        return self.check_element_displaying_or_not('ACTION_SHEETS_HEADER_NAME')

    def go_back_to_home(self):
        self.go_back()

    def tap_on_ok_cancel_button(self):
        self.click("OK_CANCEL_BUTTON_XPATH")

    def tap_on_ok_button(self):
        self.click("OK_BUTTON_NAME")

    def tap_on_cancel_button(self):
        self.click("CANCEL_BUTTON_NAME")

    def check_ok_cancel_button_displaying(self):
        return self.check_element_displaying_or_not("OK_CANCEL_BUTTON_XPATH")

    def check_other_button_displaying(self):
        return self.check_element_displaying_or_not("OTHER_BUTTON_XPATH")

    def click_other_button(self):
        self.click("OTHER_BUTTON_XPATH")

    def click_safe_choice_button(self):
        self.click('SAFE_CHOICE_BUTTON_NAME')

    def click_destructive_button(self):
        self.click('DESTRUCTIVE_BUTTON_NAME')
