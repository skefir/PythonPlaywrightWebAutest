from playwright.sync_api import Page, Locator

from data.option_filterable import OptionFilterable
from elements.common_utils import CommonUtils


class BasePage:
    def __init__(self, page: Page):
        self.page = page
        self.element_helper = CommonUtils()

    def get_current_page(self):
        return self

    def is_option_contains(self, option_set: set[OptionFilterable], label_option: str):
        return any(print("{} = {} or {} res = {}".format(label_option, elem.get_title(), elem.get_alt_title(),
                                                         elem.get_title() == label_option.strip() or elem.get_alt_title() == label_option)) or (
                           elem.get_title() == label_option or elem.get_alt_title() == label_option) for elem in
                   option_set)

    def set_filter_option(self, filter_option_element: Locator):
        self.element_helper.get_filter_option_label(filter_option_element).click()

    def set_filter_checkbox_group(self, filter_element: Locator, option_set: set[OptionFilterable]):
        self.element_helper.to_observe(self.element_helper.get_filter_options(filter_element)).subscribe(
            on_next=lambda val: self.set_filter_option_checkbox(val[1], self.is_option_contains(option_set,
                                                                                                self.element_helper.get_filter_option_label(
                                                                                                    val[
                                                                                                        1]).text_content()))
        )
        return self

    def set_filter_option_checkbox(self, filter_option_element: Locator, value: bool):
        if value != self.is_checked(filter_option_element):
            self.set_filter_option(filter_option_element)

    def is_checked(self, check_box_element: Locator) -> bool:
        return self.element_helper.get_filter_check_box(check_box_element).is_checked()
