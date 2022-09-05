"""
rill - tests
"""

import codecs
import unittest
from typing import List, Iterable

from .rill import Stream


def caesar(text: str) -> str:
    """Caesar Cypher."""
    return str(codecs.encode(text, "rot_13"))


def inp_from_str(content: str) -> Stream:
    """Simulate input from string with newlines."""

    def get() -> Iterable[str]:
        """Yield line by line."""
        for line in content.splitlines():
            yield line

    return Stream(get)


def materialize(provider: Stream) -> List[str]:
    """Collect all items from iterator and put into a list."""
    return list(provider.get_source()())


class TestMethods(unittest.TestCase):
    """Tests stream methods."""

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

    def test_line_count(self) -> None:
        """Test line count."""
        res = materialize(inp_from_str("hello\ndear world").line_count())
        self.assertEqual(1, len(res))
        self.assertEqual("2", res[0])

    def test_char_count(self) -> None:
        """Test char count."""
        res = materialize(inp_from_str("hello\ndear world").char_count())
        self.assertEqual(1, len(res))
        self.assertEqual("15", res[0])

    def test_world_count(self) -> None:
        """Test word count."""
        res = materialize(inp_from_str("hello\ndear world").word_count())
        self.assertEqual(1, len(res))
        self.assertEqual("3", res[0])
