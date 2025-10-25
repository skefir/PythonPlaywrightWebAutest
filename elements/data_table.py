import reactivex as rx
from functools import cached_property

from playwright.sync_api import Locator
from reactivex import operators as ops, Observable

from data.data_table_column import DataTableColumn
from elements.common_utils import CommonUtils


class DataTable:

    def __init__(self, root_element: Locator, classPrefix: str, column_set: set[DataTableColumn]):
        self.classPrefix = classPrefix
        self.columns = column_set
        self.root_element = root_element
        self.element_helper = CommonUtils()

    @cached_property
    def calculate_column_numbers(self) -> dict[str, int]:
        return {l.text_content().strip() if l.text_content().strip().find(
            ",") == -1 else l.text_content().strip()[:l.text_content().strip().find(","):]: i for (i, l) in
                enumerate(self.get_table_headers())}

    def get_column_number(self, column: DataTableColumn) -> int:
        assert column in self.columns, f"Illegal column - {column}"
        return self.calculate_column_numbers.get(column.get_title())

    def get_table_headers(self) -> list[Locator]:
        loc_head = self.root_element.locator(f".{self.classPrefix}__header .{self.classPrefix}__col")
        return [loc_head.nth(l) for l in range(loc_head.count())]

    def get_row_by_number(self, row_number: int) -> Locator:
        return self.__get_rows().nth(row_number - 1)

    def __get_rows(self) -> Locator:
        return self.root_element.locator(f"div.{self.classPrefix}__item")

    def get_column(self, row_element: Locator, column: DataTableColumn) -> Locator:
        return row_element.locator(f"div[class*='{self.classPrefix}__']:nth-child({self.get_column_number(column)})")

    def get_botom_area(self) -> Locator:
        return self.root_element.locator("div[class*='table__bottom']")

    def __process_page(self, page_locator: Locator) -> Observable:
        """Кликает на локатор страницы, ждет обновления и возвращает Observable со строками."""
        page_locator.click()

        # Ждем, пока первая строка таблицы снова станет видимой после перезагрузки.
        # Это предполагает, что таблица на мгновение исчезает или перерисовывается.
        self.root_element.locator(f"div.{self.classPrefix}__item").first.wait_for(state="visible", timeout=5000)
        # return rx.of(self.__get_rows().all()).pipe(ops.map(lambda pg_tuple: pg_tuple[1].text_content()))
        # return self.element_helper.to_observe(self.__get_rows())
        return self.__get_rows().all()

    def get_row_stream(self) -> Observable:
        pages_collection = self.get_botom_area().locator("a")
        all_streams = rx.concat(
            rx.of(self.__get_rows()),  # Поток для первой страницы
            self.element_helper.to_observe(pages_collection).pipe(
                ops.skip(1),
                # ops.do(lambda page_tuple: page_tuple[1].click()),
                ops.map(lambda page_tuple: self.__process_page(page_tuple[1])),
                # ops.merge(max_concurrent=1),
                # ops.map(lambda row_tuple: row_tuple[1].text_content())
                # ops.flat_map(lambda page_tuple: self.__process_page(page_tuple[1]), max_concurrent=1)
            )
        )
        # "Склеиваем" все внутренние потоки в один
        return all_streams.pipe(
            ops.concat()
        )


        # if pages_collection.count() < 1:
        #     pages_collection = self.get_botom_area()
        # return self.element_helper.to_observe(pages_collection).pipe(ops.(lambda pg: pg[1].click() or self.element_helper.to_observe(self.__get_rows())))
        # return rx.concat(self.element_helper.to_observe(pages_collection).pipe(
        #     ops.map(lambda page_tuple: page_tuple[1].click() or self.__get_rows())))

