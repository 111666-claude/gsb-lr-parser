import unittest

from lrparser.lr import GRAMMAR, LrError, evaluate, tokenize


class TokenizeTest(unittest.TestCase):
    def test_numbers_and_operators(self):
        self.assertEqual(tokenize("1+2*3"),
                         [("num", 1), ("+", "+"), ("num", 2), ("*", "*"), ("num", 3)])

    def test_parentheses(self):
        self.assertEqual(tokenize("(1)")[0][0], "(")

    def test_bad_character(self):
        with self.assertRaises(LrError):
            tokenize("1%2")


class GrammarTest(unittest.TestCase):
    def test_grammar_size(self):
        self.assertGreaterEqual(len(GRAMMAR), 6)

    def test_single_number(self):
        self.assertEqual(evaluate("7"), 7)

    def test_addition(self):
        self.assertEqual(evaluate("1+2"), 3)

    def test_empty_expression(self):
        self.assertEqual(evaluate(""), 0)


if __name__ == "__main__":
    unittest.main()
