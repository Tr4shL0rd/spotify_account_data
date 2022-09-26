import pytest
import unittest
from account_data import files
from account_data import get

class TestGet(unittest.TestCase):
    def __init__(self, methodName: str = ...) -> None:
        super().__init__(methodName)

    def test_get_control(self):
        self.assertEqual(get("Follow"), "Follow.json")

    def test_get_error(self):
        expected_exception = IndexError
        with pytest.raises(expected_exception) as exc_info:
            get("dwa")
        exc_info == expected_exception