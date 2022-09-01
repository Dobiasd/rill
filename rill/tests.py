"""
rill - tests
"""

import unittest
from typing import List, Iterable

from .rill import Provider


def inp_from_str(content: str) -> Provider:
    """Simulate input from string with newlines."""

    def get() -> Iterable[str]:
        """Yield line by line."""
        for line in content.splitlines():
            yield line

    return Provider(get)


def materialize(provider: Provider) -> List[str]:
    """Collect all items from iterator and put into a list."""
    return list(provider.get_source()())


class TestGrep(unittest.TestCase):
    """Tests grep."""

    def test_filtering_lines(self) -> None:
        """Should work."""
        res = materialize(inp_from_str("hello\nworld").grep("orl"))
        self.assertEqual(1, len(res))
        self.assertEqual("world", res[0])
