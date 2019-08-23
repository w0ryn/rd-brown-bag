class RomanNumeralConverter:
    NUMERALS = 'IVXLCDMvxlcdm' # in ascending value

    def convertIntegerToRomanNumeral(self, integer):
        max_numeral_value = self.getValueOfLargestRomanNumeral()

        converted_numeral = '';

        while integer >= max_numeral_value:
            converted_numeral += self.NUMERALS[-1]
            integer -= max_numeral_value

        digit_list = self.splitIntegerIntoListOfDigits(integer)
        digit_max_index = len(digit_list) - 1

        i = 0
        while i <= digit_max_index:
            digit = digit_list[i]
            decimal_place = digit_max_index - i

            converted_numeral += self.convertDigitToNumeral(digit, decimal_place)
            i += 1

        return converted_numeral

    def convertRomanNumeralToInteger(self, roman_numeral):
        numeral_count = len(roman_numeral)

        total = i = 0
        while i < numeral_count:
            current_numeral_value = self.getDecimalValueOfRomanNumeral(roman_numeral[i])

            if i == numeral_count - 1: 
                last_numeral_value = current_numeral_value
                total += last_numeral_value # last numeral can't be a subtract numeral
            else:
                next_numeral_value = self.getDecimalValueOfRomanNumeral(roman_numeral[i + 1])
                if current_numeral_value >= next_numeral_value:
                    total += current_numeral_value
                else:
                    total -= current_numeral_value

            i += 1

        return int(total)

    def getValueOfLargestRomanNumeral(self):
        return self.getDecimalValueOfRomanNumeral(self.NUMERALS[-1])

    def getDecimalValueOfRomanNumeral(self, numeral):
        numeral_index = self.NUMERALS.find(numeral)
        numeral_is_a_power_of_ten = numeral_index % 2 == 0

        power_of_ten = int(numeral_index / 2)
        if numeral_is_a_power_of_ten:
            return 10**power_of_ten # e.g. I = 1, X = 10, C = 100, etc.
        return 5 * 10**power_of_ten # e.g. V = 5, L = 50, D = 500, etc.

    def splitIntegerIntoListOfDigits(self, integer):
        return [ int(digit) for digit in str(int(integer)) ]

    def convertDigitToNumeral(self, digit, decimal_place):
        # decimal_place :: 1s = 0, 10s = 1, 100s = 2, etc.
        index = 2 * decimal_place

        # e.g. 'IVX', 'XLC', 'CDM', etc
        RELATIVE_NUMERALS = ( self.NUMERALS[index] + self.NUMERALS[index + 1] + self.NUMERALS[index + 2] )

        converted_digit = ''
        if digit == 9:
            converted_digit += RELATIVE_NUMERALS[0] + RELATIVE_NUMERALS[2] # IX
            digit -= 9
        if digit == 4:
            converted_digit += RELATIVE_NUMERALS[0] + RELATIVE_NUMERALS[1] # IV
            digit -= 4
        if digit >= 5:
            converted_digit += RELATIVE_NUMERALS[1] # V
            digit -= 5

        for i in range(digit): # I, II, or III
            converted_digit += RELATIVE_NUMERALS[0]

        return converted_digit
