import re

import allure
from playwright.sync_api import Page, expect

from data.date_filter_option import DateFilterOption
from data.importance_filter_option import ImportanceFilterOption
from data.currencies import Currencies
from page.calendar_list_page import CalendarListPage
import pytest
import time


@pytest.mark.browser_context_args(timezone_id="Europe/Berlin", locale="en-GB", )
@allure.title("Test event calendar")
def test_has_title(page: Page):
    page.goto("https://www.mql5.com/en/economic-calendar")

    calendar_option = DateFilterOption.NEXT_MONTH
    importance_set = {ImportanceFilterOption.MEDIUM}
    currency_set = {Currencies.CHF}
    list_page = CalendarListPage(page)
    (list_page.set_date_filter(calendar_option)
     .set_importance_filter(importance_set)
     .set_currencies_filter(currency_set)
     .enter_to_event_by_number(1))

    time.sleep(10)
    page.screenshot(path="exp3.png")



def test_get_started_link(page: Page):
    page.goto("https://playwright.dev/")

    # Click the get started link.
    page.get_by_role("link", name="Get started").click()

    # Expects page to have a heading with the name of Installation.
    expect(page.get_by_role("heading", name="Installation")).to_be_visible()

