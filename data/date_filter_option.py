from datetime import date

from dateutil.relativedelta import relativedelta, MO, SU

from data.option_filterable import OptionFilterable
from util.date_convert import first_day_of_month, last_day_of_month


class DateFilterOption(OptionFilterable):
    CURRENT_WEEK = ("Current week", 0)
    PREVIOUS_WEEK = ("Previous week", -1)
    NEXT_WEEK = ("Next week", 1)

    # Месяцы (смещение: 0 для текущего, -1 для предыдущего, +1 для следующего)
    CURRENT_MONTH = ("Current month", 0)
    PREVIOUS_MONTH = ("Previous month", -1)
    NEXT_MONTH = ("Next month", 1)

    # Метод-инициализатор для создания экземпляров
    def __init__(self, title: str, offset: int):
        self._title = title
        self._offset = offset  # Смещение (недели или месяцы)

    @property
    def today(self) -> date:
        """Возвращает текущую дату на момент вызова."""
        return date.today()

    @property
    def begin_period(self) -> date:
        """Динамически вычисляет начальную дату периода (аналог beginPeriod)."""

        # --- Логика для Недель ---
        if 'WEEK' in self.name:
            # Находим опорную дату со смещением
            target_date = self.today + relativedelta(weeks=self._offset)
            # Ищем ближайший понедельник к опорной дате
            return target_date + relativedelta(weekday=MO(-1))

        # --- Логика для Месяцев ---
        elif 'MONTH' in self.name:
            # Находим опорную дату со смещением
            target_date = self.today + relativedelta(months=self._offset)
            # Возвращаем первый день этого месяца
            return first_day_of_month(target_date)

    @property
    def finish_period(self) -> date:
        """Динамически вычисляет конечную дату периода (аналог finishPeriod)."""

        # --- Логика для Недель ---
        if 'WEEK' in self.name:
            # Находим опорную дату со смещением
            target_date = self.today + relativedelta(weeks=self._offset)
            # Ищем ближайшее воскресенье к опорной дате
            return target_date + relativedelta(weekday=SU(+1))

        # --- Логика для Месяцев ---
        elif 'MONTH' in self.name:
            # Находим опорную дату со смещением
            target_date = self.today + relativedelta(months=self._offset)
            # Возвращаем последний день этого месяца
            return last_day_of_month(target_date)

    def __str__(self) -> str:
        """Аналог Kotlin toString()."""
        # Используем .value[0] для доступа к title, если не использовать @property
        return f"{self.name} - ({self.begin_period}, {self.finish_period})"

    def get_title(self):
        return self.value[0]

