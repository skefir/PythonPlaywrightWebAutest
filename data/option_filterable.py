from enum import Enum


class OptionFilterable(Enum):
    def get_title(self):
        return self.value

    def get_alt_title(self):
        return f"{self.name} - {self.value}"
