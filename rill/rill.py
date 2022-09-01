"""
rill
"""

import fileinput
from typing import Iterable, Callable


class Provider:
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

    def grep(self, needle: str) -> "Provider":
        """Grep functionality."""

        def get() -> Iterable[str]:
            """Filter lines."""
            for line in self._source():
                if needle in line:
                    yield line

        return Provider(get)

    def map_lines(self, func: Callable[[str], str]) -> "Provider":
        """Transform lines one by one."""

        def get() -> Iterable[str]:
            """Apply function to each line."""
            for line in self._source():
                yield func(line)

        return Provider(get)

    def line_lengths(self) -> "Provider":
        """Get the length of each line."""

        def length(line: str) -> str:
            """Line-length helper."""
            return str(len(line))

        return self.map_lines(length)

    def replace(self, frm: str, target: str) -> "Provider":
        """SED-like text replacement."""

        def get() -> Iterable[str]:
            """Transform line by line."""
            for line in self._source():
                yield line.replace(frm, target)

        return Provider(get)

    def line_count(self) -> "Provider":
        """WC-l-like line counting."""

        def get() -> Iterable[str]:
            """Transform line by line."""
            yield str(len(list(self._source())))

        return Provider(get)

    # to implement:
    # - regex grep
    # - regex replace
    # - word count
    # - char count
    # - sum
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


def inp() -> Provider:
    """Entry point to construct a stream from an input."""

    def get() -> Iterable[str]:
        """Iterate line by line, removing trailing newline characters."""
        for line in fileinput.input():
            yield line.rstrip()

    return Provider(get)
