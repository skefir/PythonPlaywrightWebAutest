from playwright.sync_api import Page

from data.importance_filter_option import ImportanceFilterOption
from elements.calendar_list_elements import CalendarListElements
from page.base_page import BasePage


class CalendarListPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)
        self.element_helper = CalendarListElements(page)

    def set_importance_filter(self, importance_set: set[ImportanceFilterOption]) :
        self.set_filter_checkbox_group(self.element_helper.get_importance_filter(), importance_set)
        return self



