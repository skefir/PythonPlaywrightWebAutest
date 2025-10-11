from typing import Self

from playwright.sync_api import Page

from data.calendar_event_info_tab import CalendarEventInfoTab
from data.currencies import Currencies
from data.importance_filter_option import ImportanceFilterOption
from elements.calendar_event_elements import CalendarEventElements
from elements.tab_control import TabControl
from page.base_page import BasePage


class CalendarEventInfoPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.element_helper = CalendarEventElements(page)
        self.tab_control = TabControl(self.element_helper.get_event_tab_control())

    def goto_tab(self, tab: CalendarEventInfoTab):
        self.tab_control.getTab(tab).click()

    def check_importance(self, importance_set: set[ImportanceFilterOption]) -> Self:
        assert self.is_option_contains(importance_set, self.element_helper.get_event_importance().text_content())
        return self

    def check_currency(self, currencies_set: set[Currencies] ):
        assert self.is_option_contains(currencies_set, self.element_helper.get_event_currency())
