from playwright.sync_api import Page, Locator

from data.calendar_event_info_tab import CalendarEventInfoTab
from elements.common_utils import CommonUtils
from elements.data_table import DataTable


class CalendarEventElements(CommonUtils):
    def __init__(self, _page: Page):
        self.page = _page
        self.event_history_table = DataTable(self.get_event_history_table(), "event-table-history",
                                             {e for e in CalendarEventInfoTab})

    def get_event_root(self) -> Locator:
        return self.page.locator("#eventContentPanel")

    def get_event_currency(self) -> Locator:
        return self.get_event_root().locator(".economic-calendar__event-header-currency")

    def get_event_importance(self) -> Locator:
        return self.get_event_root().locator(".event-table__importance")

    def get_event_date(self) -> Locator:
        return self.get_event_root().locator("td#actualValueDate")

    def get_event_tab_control(self) -> Locator:
        return self.get_event_root().locator("ul#calendar-tabs")

    def get_event_history_table(self) -> Locator:
        return self.get_event_root().locator("#tab_content_history")
