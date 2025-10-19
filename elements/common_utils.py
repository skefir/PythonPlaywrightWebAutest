import reactivex as rx
from reactivex import operators as ops, Observable

from playwright.sync_api import Locator

from data.option_filterable import OptionFilterable


class CommonUtils:

    def to_observe(self, locator: Locator) -> Observable:
        length = locator.count()
        if length < 0:
            return rx.empty()
        return rx.range(0, length).pipe(
            ops.map(lambda i: (i, locator.nth(i)))
        )

    def get_filter_options(self, root_element: Locator) -> Locator:
        return root_element.locator("li:visible")

    def get_filter_check_box(self, filter_option_element: Locator) -> Locator:
        return filter_option_element.locator("input[type='checkbox']")

    def get_filter_option(self, root_filter_element: Locator, option: OptionFilterable) -> Locator:
        return root_filter_element.locator(f"li label:has-text('{option.get_title()}')")

    def get_filter_option_label(self, filter_options_element: Locator) -> Locator:
        return filter_options_element.locator("label")

