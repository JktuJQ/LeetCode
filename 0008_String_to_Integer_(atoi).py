class Solution:
    def myAtoi(self, s: str) -> int:
        result = 0

        start = 0
        while start < len(s) and s[start] == " ":
            start += 1

        sign = 1
        if start >= len(s):
            return result
        if s[start] in ("+", "-"):
            if s[start] == "-":
                sign = -1
            start += 1
        if start >= len(s):
            return result

        while start < len(s) and s[start].isnumeric():
            result *= 10
            result += int(s[start])
            start += 1
        result *= sign

        UPPER_BOUND = 2 ** 31 - 1
        LOWER_BOUND = -(2 ** 31)
        result = max(LOWER_BOUND, min(result, UPPER_BOUND))
        return result
