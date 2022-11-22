#!/usr/bin/python3
"""
  The Test File for the Console
"""
import unittest
import pep8


class tests_Console(unittest.TestCase):
    """
      The Unittest
    """

    def test_pep8_conformance(self):
        """
          The Test pep8
        """
        pep8_style = pep8.StyleGuide(quiet=True)
        result = pep8_style.check_files(['console.py'])
        self.assertEqual(
            result.total_errors, 0, "Found code style errors (and warnings).")
