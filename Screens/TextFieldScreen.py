from Screens.BasePage import BasePage


class TextFieldScreen(BasePage):

    def __int__(self, driver):
        super().__init__(driver)

    def check_header_displaying(self) -> bool:
        """
        Check 'Text Fields' Header is displaying or not
        :return: boolean value of 'True' or 'False'
        """

        return self.check_element_displaying_or_not('TEXT_FIELD_HEADER_XPATH')

    def go_back_to_home(self):
        """
        Navigate Back to Home Page

        """
        self.go_back()

    def check_default_text_field_header_displaying(self) -> bool:
        """

        :return:
        """
        return self.check_element_displaying_or_not('DEFAULT_TEXT_FIELD_HEADER_NAME')

    def check_tinted_text_field_header_displaying(self):
        return self.check_element_displaying_or_not('TINTED_TEXT_FIELD_HEADER_NAME')

    def check_secure_text_field_header_displaying(self):
        return self.check_element_displaying_or_not('SECURE_TEXT_FIELD_HEADER_NAME')

    def check_specific_keyword_text_field_header_displaying(self):
        return self.check_element_displaying_or_not('SPECIFIC_KEYBOARD_TEXT_FIELD_HEADER_NAME')

    def check_custom_text_field_header_displaying(self):
        return self.check_element_displaying_or_not('CUSTOM_TEXT_FIELD_HEADER_NAME')

    def check_default_text_field_displaying(self):
        return self.check_element_displaying_with_index_or_not('INPUT_FIELD_CLASS_NAME', 0)

    def check_tinted_text_field_displaying(self):
        return self.check_element_displaying_with_index_or_not('INPUT_FIELD_CLASS_NAME', 1)

    def check_specific_keyword_text_field_displaying(self):
        return self.check_element_displaying_with_index_or_not('INPUT_FIELD_CLASS_NAME', 2)

    def check_custom_text_field_displaying(self):
        return self.check_element_displaying_with_index_or_not('INPUT_FIELD_CLASS_NAME', 3)

    def check_secure_text_field_displaying(self):
        return self.check_element_displaying_or_not('SECURE_FIELD_CLASS_NAME')

    def enter_value_on_default_text_field(self, value):
        self.send_text_with_index('INPUT_FIELD_CLASS_NAME', 0, value)

    def enter_value_on_tinted_text_field(self, value):
        self.send_text_with_index('INPUT_FIELD_CLASS_NAME', 1, value)

    def enter_value_on_specific_keyword_text_field(self, value):
        self.send_text_with_index('INPUT_FIELD_CLASS_NAME', 2, value)

    def enter_value_on_custom_text_field(self, value):
        self.send_text_with_index('INPUT_FIELD_CLASS_NAME', 3, value)

    def enter_value_on_secure_field(self, value):
        self.send_text('SECURE_FIELD_CLASS_NAME', value)

    def get_value_from_default_text_field(self):
        return self.get_attribute_value_of_element_with_index('INPUT_FIELD_CLASS_NAME', 'value', 0)

    def get_value_from_tinted_text_field(self):
        return self.get_attribute_value_of_element_with_index('INPUT_FIELD_CLASS_NAME', 'value', 1)

    def get_value_from_specific_keyword_text_field(self):
        return self.get_attribute_value_of_element_with_index('INPUT_FIELD_CLASS_NAME', 'value', 2)

    def get_value_from_custom_text_field(self):
        return self.get_attribute_value_of_element_with_index('INPUT_FIELD_CLASS_NAME', 'value', 3)

    def get_value_from_secure_text_field(self):
        return self.get_attribute_value_of_element('SECURE_FIELD_CLASS_NAME', 'value')

    def click_on_cross_button_on_secure_text(self):
        self.click('CLEAR_TEXT_BUTTON_OF_SECURE_FIELD_XPATH')
