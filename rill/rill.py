"""
rill
"""

import fileinput
from typing import Iterable, Callable


class Stream:
    """The main class providing method chaining."""

    def __init__(self, source: Callable[[], Iterable[str]]):
        """Set source."""
        self._source = source

    def get_source(self) -> Callable[[], Iterable[str]]:
        """Return source for external access."""
        return self._source

    def show(self) -> None:
        """Print everything."""
        for line in self._source():
            print(line)

    def grep(self, needle: str) -> "Stream":
        """Grep functionality."""

        def get() -> Iterable[str]:
            """Filter lines."""
            for line in self._source():
                if needle in line:
                    yield line

        return Stream(get)

    def map_lines(self, func: Callable[[str], str]) -> "Stream":
        """Transform lines one by one."""

        def get() -> Iterable[str]:
            """Apply function to each line."""
            for line in self._source():
                yield func(line)

        return Stream(get)

    def line_lengths(self) -> "Stream":
        """Get the length of each line."""

        def length(line: str) -> str:
            """Line-length helper."""
            return str(len(line))

        return self.map_lines(length)

    def replace(self, frm: str, target: str) -> "Stream":
        """SED-like text replacement."""

        def get() -> Iterable[str]:
            """Transform line by line."""
            for line in self._source():
                yield line.replace(frm, target)

        return Stream(get)

    def line_count(self) -> "Stream":
        """WC-l-like line counting."""

        def get() -> Iterable[str]:
            """Transform line by line."""
            yield str(len(list(self._source())))

        return Stream(get)

    def char_count(self) -> "Stream":
        """WC-m-like line counting."""

        def get() -> Iterable[str]:
            """Sum up chars of all lines."""
            yield str(sum(map(len, self._source())))

        return Stream(get)

    def word_count(self) -> "Stream":
        """WC-w-like line counting."""

        def get() -> Iterable[str]:
            """Split each line into words and sum up."""
            yield str(sum(map(lambda line: len(line.split()), self._source())))

        return Stream(get)

    # to implement:
    # - regex grep
    # - regex replace
    # - sort
    # - sort numerical
    # - reverselines
    # - reversechars
    # - toupper
    # - tolower
    # - split
    # - head
    # - tail
    # - uniq
    # - tr
    # - select column by separator


def inp() -> Stream:
    """Entry point to construct a stream from an input."""

    def get() -> Iterable[str]:
        """Iterate line by line, removing trailing newline characters."""
        for line in fileinput.input():
            yield line.rstrip()

    return Stream(get)
