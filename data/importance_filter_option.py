from enum import Enum

from data.option_filterable import OptionFilterable


class ImportanceFilterOption(Enum):
    HOLIDAYS = OptionFilterable("Holidays")
    LOW = OptionFilterable("Low")
    MEDIUM = OptionFilterable("Medium")
    HIGH = OptionFilterable("High")


