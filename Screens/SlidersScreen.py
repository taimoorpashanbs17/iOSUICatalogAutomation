from Screens.BasePage import BasePage


class SlidersScreen(BasePage):
    def __int__(self, driver):
        super().__init__(driver)

    def check_header_displaying(self):
        return self.check_element_displaying_or_not('SLIDERS_HEADER_XPATH')

    def check_default_slider_header_displaying(self):
        return self.check_element_displaying_or_not('DEFAULT_SLIDER_HEADER_XPATH')

    def check_tinted_slider_header_displaying(self):
        return self.check_element_displaying_or_not('TINTED_SLIDER_HEADER_XPATH')

    def check_custom_slider_header_displaying(self):
        return self.check_element_displaying_or_not('CUSTOM_SLIDER_HEADER_XPATH')

    def move_default_slider(self, value):
        self.send_text_with_index('SLIDERS_CLASS_NAME', 0, value)

    def move_tinted_slider(self, value):
        self.send_text_with_index('SLIDERS_CLASS_NAME', 1, value)

    def move_custom_slider(self, value):
        self.send_text_with_index('SLIDERS_CLASS_NAME', 2, value)

    def go_back_to_home(self):
        self.go_back()

    def get_default_slider_value(self):
        return self.get_attribute_value_of_element_with_index('SLIDERS_CLASS_NAME', 'value', 0)[0:2]

    def get_tinted_slider_value(self):
        return self.get_attribute_value_of_element_with_index('SLIDERS_CLASS_NAME', 'value', 1)[0:2]

    def get_custom_slider_value(self):
        return self.get_attribute_value_of_element_with_index('SLIDERS_CLASS_NAME', 'value', 2)[0:2]
