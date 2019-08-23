import re

from roman_numeral_converter import RomanNumeralConverter
from ordered_set import OrderedSet


class SampleExercises:
    @staticmethod
    def get_roman_numeral(int_number):
        rnc = RomanNumeralConverter()
        return rnc.convertIntegerToRomanNumeral(int_number)

    @staticmethod
    def convert_roman_numeral(roman_numeral):
        rnc = RomanNumeralConverter()
        return rnc.convertRomanNumeralToInteger(roman_numeral)

    @staticmethod
    def remove_duplicate_words(phrase):
        # return ' '.join(set(phrase.split())
        #
        # unfortunately, a standard set does not maintain the order of keys entered.
        # python's `collections` library, however has an OrderedDict, which can be used
        # to implement an 'OrderedSet'

        return str(OrderedSet(phrase.split())) # a standard set does not maintain order

    @staticmethod
    def dict_replacer(phrase, dictionary):
        replace_me = re.compile('(<([^>]*)>)')

        for match in replace_me.findall(phrase):
            phrase = re.compile(match[0]).sub(dictionary[match[1]], phrase)

        return phrase
