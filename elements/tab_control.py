from playwright.sync_api import Locator

from data.control_tab_entity import ControlTabEntity


class TabControl[T : ControlTabEntity]:
    def __init__(self, root_element: Locator):
        self.root_element = root_element

    def  getTab(self, tab: T) -> Locator:
        return self.root_element.locator(f"li:has-text('{tab.get_title()}')")