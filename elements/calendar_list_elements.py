from playwright.sync_api import Locator, Page

from elements.common_utils import CommonUtils


class CalendarListElements(CommonUtils):
    def __init__(self, _page: Page):
        self.page = _page

    def get_calendar_root(self) -> Locator:
        return self.page.locator("#calendarContainer")

    def get_filter_area(self)->Locator:
        return self.get_calendar_root().locator("#economicCalendarFilter")

    def get_currencies_filter(self) -> Locator:
        return self.get_filter_area().locator("ul#economicCalendarFilterCurrency")

    def get_importance_filter(self) -> Locator:
        return self.get_filter_area().locator("ul#economicCalendarFilterImportance")

    def get_date_filter(self) -> Locator:
        return self.get_filter_area().locator("ul#economicCalendarFilterDate")

    def get_main_table(self) -> Locator:
        return self.get_calendar_root().locator("xpath=.//div[@class='ec-table' and .//div[@id='economicCalendarTable']]")

    # fun getMainTable(): Locator =
    # getCalendarRoot().locator("xpath=.//div[@class='ec-table' and .//div[@id='economicCalendarTable']]")