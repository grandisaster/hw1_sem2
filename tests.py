import unittest
from unittest.mock import patch
from main import *


class TestingNotes(unittest.TestCase):

    def test_wrong_id(self):
        with patch('builtins.input', side_effect=[0]):
            self.assertEqual(modification(), (print('Id is not found')))

    def test_empty_notes_search(self):
        with patch('builtins.input', side_effect=["nice"]):
            self.assertEqual(searching(), None)

    def test_addition(self):
        with patch('builtins.input', side_effect=["kek", 'lol']):
            self.assertEqual(addition(), print("Your note has been added."))

    def test_choice_value_error(self):
        with patch('builtins.input', side_effect=['e3']):
            with self.assertRaises(ValueError):
                app()

    def test_modification_error(self):
        with patch('builtins.input', side_effect=['w']):
            with self.assertRaises(ValueError):
                modification()


if __name__ == '__main__':
    unittest.main()
