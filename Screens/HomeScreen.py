from Screens.BasePage import BasePage


class HomeScreen(BasePage):
    """
        All Action items of Home Screen will be mentioned there.
    """

    def __int__(self, driver):
        super().__init__(driver)

    def click_on_action_sheets_link(self):
        """
            Click on Action Sheets Link.
        """

        self.click('action_sheets_link_XPATH')

    def check_ui_catalog_header_displaying(self) -> bool:
        """
            Check that 'UICatalog' Header displaying or not.
        :return: Boolean of 'True' or 'False', in case header is displaying or not.
        """

        return self.check_element_displaying_or_not("UI_CATALOG_HEADER_XPATH")

    def click_on_sliders_link(self):
        """
            Click on Sliders Link.
        """

        self.click('SLIDERS_LINK_XPATH')

    def click_on_text_fields_link(self):
        """
            Scroll down to Action Text Fields link and Click it.
        """

        self.scroll_up_down_till_text_shown('TEXT_FIELDS_LINK_XPATH', 16, 478, 126)
        self.click('TEXT_FIELDS_LINK_XPATH')

    def click_on_date_picker_link(self):
        """
            Click on Date Picker Link.
        """

        self.click('DATE_PICKER_LINK_XPATH')
