from calendar import Calendar

from playwright.sync_api import Page

from data.date_filter_option import DateFilterOption
from data.importance_filter_option import ImportanceFilterOption
from data.currencies import Currencies
from elements.calendar_list_elements import CalendarListElements
from page.base_page import BasePage


class CalendarListPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)
        self.element_helper = CalendarListElements(page)

    def set_importance_filter(self, importance_set: set[ImportanceFilterOption]):
        self.set_filter_checkbox_group(self.element_helper.get_importance_filter(), importance_set)
        return self

    def set_currencies_filter(self, currencies_set: set[Currencies]):
        self.set_filter_checkbox_group(self.element_helper.get_currencies_filter(), currencies_set)
        return self

    def set_date_filter(self, calendar_option: DateFilterOption):
        self.element_helper.get_filter_option(self.element_helper.get_date_filter(), calendar_option).click()
        return self
