from enum import Enum


class DataTableColumn(Enum):
    def get_title(self):
        return self.value

    def get_column_by_title(self, column_name: str):
        return DataTableColumn(column_name)