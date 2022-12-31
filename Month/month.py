import datetime


class Month:
    __slots__ = ("_year", "_month",)

    def __init__(self, year: int, month: int):
        self._year = year
        self._month = month

    @classmethod
    def from_date(cls, date_obj: datetime.date):
        return Month(date_obj.year, date_obj.month)

    @property
    def year(self):
        return self._year

    @property
    def month(self):
        return self._month

    @property
    def first_day(self):
        return datetime.date(year=self.year, month=self.month, day=1)

    @property
    def last_day(self):
        next_month = datetime.date(year=self.year, month=self.month + 1, day=1)
        return next_month - datetime.timedelta(days=1)

    def strftime(self, fmt: str):
        return self.first_day.strftime(fmt)

    def __eq__(self, other: "Month"):
        if not isinstance(other, Month):
            return False
        return self.month == other.month and self.year == other.year

    def __lt__(self, other: "Month") -> bool:
        if not isinstance(other, Month):
            raise TypeError
        return self.year < other.year

    def __le__(self, other: "Month") -> bool:
        if not isinstance(other, Month):
            raise TypeError
        return self.year <= other.year

    def __str__(self):
        month_str = str(self.month) if self.month > 9 else f"0{self.month}"
        return f"{self.year}-{month_str}"

    def __repr__(self):
        return f"Month({self.year}, {self.month})"

    def __hash__(self):
        return hash(repr(self))


if __name__ == '__main__':
    python2_eol = Month(2020, 1)
    print(python2_eol == datetime.date(2020, 1, 1))
