"""
rill - tests
"""

import codecs
import unittest
from typing import List, Iterable

from .rill import Provider


def caesar(text: str) -> str:
    """Caesar Cypher."""
    return str(codecs.encode(text, "rot_13"))


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


class TestMethods(unittest.TestCase):
    """Tests methods."""

    def test_grep(self) -> None:
        """Test filtering lines."""
        res = materialize(inp_from_str("hello\nworld").grep("orl"))
        self.assertEqual(1, len(res))
        self.assertEqual("world", res[0])

    def test_line_lengths(self) -> None:
        """Test char counts."""
        res = materialize(inp_from_str("hi\nworld").line_lengths())
        self.assertEqual(2, len(res))
        self.assertEqual("2", res[0])
        self.assertEqual("5", res[1])

    def test_map_lines(self) -> None:
        """Test transforming with a user function."""
        res = materialize(inp_from_str("bonjour\nrill").map_lines(caesar))
        self.assertEqual(2, len(res))
        self.assertEqual("obawbhe", res[0])
        self.assertEqual("evyy", res[1])
