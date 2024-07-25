class Solution:
    def romanToInt(self, s: str) -> int:
        symbols = {
            "I": 1,
            "IV": 4,
            "V": 5,
            "IX": 9,
            "X": 10,
            "XL": 40,
            "L": 50,
            "XC": 90,
            "C": 100,
            "CD": 400,
            "D": 500,
            "CM": 900,
            "M": 1000,
        }

        result = 0
        index = 0
        while index != len(s):
            if index + 1 < len(s):
                double = s[index] + s[index + 1]
                if double in symbols:
                    result += symbols[double]
                    index += 2
                    continue
            result += symbols[s[index]]
            index += 1
        
        return result
