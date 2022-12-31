from itertools import chain


class PiecewiseRange:
    def __init__(self, range_string: str):
        self.range_string = range_string
        self.ranges = []
        self._parse_range_string()

    def _parse_range_string(self):
        """Parses the range string and stores the resulting ranges in a list."""
        # Split the range string into a list of individual ranges
        range_strings = self.range_string.split(',')

        # Parse each range string and store the resulting range in the list
        start = end = None
        for range_string in range_strings:
            if "-" in range_string:
                start_, end_ = range_string.split('-')
            else:
                start_ = end_ = range_string

            if start is None:
                start = int(start_)
            if end is None:
                end = int(end_)
            elif int(start_) == end + 1:
                if start_ == end_:
                    end = int(start_)
                else:
                    end = int(end_)
            else:
                self.ranges.append(range(start, end + 1))  # Range is exclusive, so we need to add 1 to the end value
                start = int(start_)
                end = int(end_)
        self.ranges.append(range(start, end + 1))

    def __iter__(self):
        return chain.from_iterable(self.ranges)

    def __len__(self):
        """Returns the total number of elements in the piecewise range."""
        return sum(len(r) for r in self.ranges)

    def __getitem__(self, index):
        """Returns the element at the specified index in the piecewise range."""
        if index < 0:
            index += len(self)
        if index < 0 or index >= len(self):
            raise IndexError("Index out of range")

        for r in self.ranges:
            if index < len(r):
                return r[index]
            index -= len(r)

    def __repr__(self):
        """Returns a string representation of the piecewise range."""

        repr_ = ','.join([f"'{val.start}-{val.stop - 1}'" if val.stop - val.start > 1 else f"'{val.start}'"
                         for val in self.ranges])
        return f"PiecewiseRange({repr_})"

    def __eq__(self, other):
        """Returns True if the two piecewise ranges are equivalent, False otherwise."""
        if not isinstance(other, PiecewiseRange):
            return False
        return repr(self) == repr(other)
