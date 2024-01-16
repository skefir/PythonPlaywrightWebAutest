from enum import Enum

from data.OptionFilterable import OptionFilterable


class ImportanceFilterOption(OptionFilterable, Enum):
    HOLIDAYS = OptionFilterable("Holidays")
    LOW = OptionFilterable("Low")
    MEDIUM = OptionFilterable("Medium")
    HIGH = OptionFilterable("High")


