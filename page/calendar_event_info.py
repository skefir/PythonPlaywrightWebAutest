from playwright.sync_api import Page

from data.calendar_event_info_tab import CalendarEventInfoTab
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
