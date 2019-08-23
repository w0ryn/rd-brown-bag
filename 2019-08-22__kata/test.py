import unittest
from exercises import SampleExercises as se


class SimpleTest(unittest.TestCase):
    # Remove duplicate words
    def test_remove_duplicate_words_none_exist(self):
        phrase = 'alpha'
        result = se.remove_duplicate_words(phrase)
        self.assertEqual('alpha', result)

    def test_remove_duplicate_words_one_duplicate(self):
        phrase = 'alpha beta alpha'
        result = se.remove_duplicate_words(phrase)
        self.assertEqual('alpha beta', result)

    def test_remove_duplicate_words_multiple_duplicates(self):
        phrase = 'alpha beta alpha alpha beta delta alpha'
        result = se.remove_duplicate_words(phrase)
        self.assertEqual('alpha beta delta', result)


    # Dictionary replacer
    def test_dict_replacer_no_phrase(self):
        phrase = ''
        dictionary = {}
        result = se.dict_replacer(phrase, dictionary)
        self.assertEqual('', result)

    def test_dict_replacer_one_item_phrase(self):
        phrase = '<a>'
        dictionary = {
            'a': 'successful'
        }
        result = se.dict_replacer(phrase, dictionary)
        self.assertEqual('successful', result)

    def test_dict_replacer_two_items_phrase(self):
        phrase = 'I think <1> lives in <2>.'
        dictionary = {
            '1': 'Nate',
            '2': 'Idaho'
        }
        result = se.dict_replacer(phrase, dictionary)
        self.assertEqual('I think Nate lives in Idaho.', result)


    # Integer to Roman numeral
    def test_get_roman_numeral_one(self):
        roman_numeral = se.get_roman_numeral(1)
        self.assertEqual('I', roman_numeral)

    def test_get_roman_numeral_three(self):
        roman_numeral = se.get_roman_numeral(3)
        self.assertEqual('III', roman_numeral)

    def test_get_roman_numeral_four(self):
        roman_numeral = se.get_roman_numeral(4)
        self.assertEqual('IV', roman_numeral)

    def test_get_roman_numeral_five(self):
        roman_numeral = se.get_roman_numeral(5)
        self.assertEqual('V', roman_numeral)

    def test_get_roman_numeral_six(self):
        roman_numeral = se.get_roman_numeral(6)
        self.assertEqual('VI', roman_numeral)

    def test_get_roman_numeral_nine(self):
        roman_numeral = se.get_roman_numeral(9)
        self.assertEqual('IX', roman_numeral)

    def test_get_roman_numeral_ten(self):
        roman_numeral = se.get_roman_numeral(10)
        self.assertEqual('X', roman_numeral)

    # Roman numeral to Integer
    def test_convert_roman_numeral_one(self):
        roman_numeral = se.convert_roman_numeral('I')
        self.assertEqual(1, roman_numeral)

    def test_convert_roman_numeral_three(self):
        roman_numeral = se.convert_roman_numeral('III')
        self.assertEqual(3, roman_numeral)

    def test_convert_roman_numeral_four(self):
        roman_numeral = se.convert_roman_numeral('IV')
        self.assertEqual(4, roman_numeral)

    def test_convert_roman_numeral_five(self):
        roman_numeral = se.convert_roman_numeral('V')
        self.assertEqual(5, roman_numeral)

    def test_convert_roman_numeral_six(self):
        roman_numeral = se.convert_roman_numeral('VI')
        self.assertEqual(6, roman_numeral)

    def test_convert_roman_numeral_nine(self):
        roman_numeral = se.convert_roman_numeral('IX')
        self.assertEqual(9, roman_numeral)

    def test_convert_roman_numeral_ten(self):
        roman_numeral = se.convert_roman_numeral('X')
        self.assertEqual(10, roman_numeral)

def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(SimpleTest)
    unittest.TextTestRunner(verbosity=2).run(suite)

main()
