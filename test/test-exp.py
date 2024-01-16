import re
from playwright.sync_api import Page, expect

from data.ImportanceFilterOption import ImportanceFilterOption
from page.CalendarListPage import CalendarListPage


# from data import ImportanceFilterOption


 # from data.ImportanceFilterOption import ImportanceFilterOption
# from page.CalendarListPage import CalendarListPage


def test_has_title(page: Page):

    page.goto("https://www.mql5.com/en/economic-calendar")

    importance_set = {ImportanceFilterOption['MEDIUM']}
    list_page = CalendarListPage(page)
    list_page.set_importance_filter(importance_set)
    page.screenshot(path="exp1.png")



def test_get_started_link(page: Page):
    page.goto("https://playwright.dev/")

    # Click the get started link.
    page.get_by_role("link", name="Get started").click()

    # Expects page to have a heading with the name of Installation.
    expect(page.get_by_role("heading", name="Installation")).to_be_visible()

