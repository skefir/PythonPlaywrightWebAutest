from datetime import timedelta, datetime
from typing import Self

import allure
import pytz
from dateutil.tz import tz
from playwright.sync_api import Page

from data.calendar_event_info_tab import CalendarEventInfoTab
from data.currencies import Currencies
from data.date_filter_option import DateFilterOption
from data.importance_filter_option import ImportanceFilterOption
from elements.calendar_event_elements import CalendarEventElements
from elements.tab_control import TabControl
from page.base_page import BasePage
from util.date_convert import convert_str_to_datetime, MIDNIGHT_TIME


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

    def check_currency(self, currencies_set: set[Currencies]):
        assert self.is_option_contains(currencies_set, self.element_helper.get_event_currency().text_content())

    @allure.step("Проверяем что событие попадает в заданный интервал дат {0}")
    def print_history_to_log(self):
        self.element_helper.event_history_table.get_row_stream().subscribe(on_next=lambda rw: print(f"row = {rw} content = {rw[1].text_content()}"))

    @allure.step("Проверяем что событие попадает в заданный интервал дат {0}")
    def check_date(self, date_filter_option: DateFilterOption):
        self.page.wait_for_load_state(state='networkidle', timeout=5000)
        print(f"event_date_loc = {self.element_helper.get_event_date()}")
        print(f"event_date_str = {self.element_helper.get_event_date().text_content()}")
        event_date = convert_str_to_datetime(self.element_helper.get_event_date().text_content())
        print(f"event_date = {event_date}")
        system_tz = tz.gettz()
        start_date_check = datetime.combine(date_filter_option.begin_period - timedelta(days=1),
                                            MIDNIGHT_TIME).astimezone(system_tz)

        finish_date_check = datetime.combine(date_filter_option.finish_period + timedelta(days=1),
                                             MIDNIGHT_TIME).astimezone(system_tz)
        is_within_period = (event_date > start_date_check) and (event_date < finish_date_check)
        assert is_within_period, (
            f"Дата события {event_date} должна находиться в периоде {date_filter_option}. "
            f"Проверяемый диапазон: ({start_date_check} - {finish_date_check})"
        )

