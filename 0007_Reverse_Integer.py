class Solution:
    def reverse(self, x: int) -> int:
        UPPER_BOUND = 2 ** 31 - 1

        sign = -1 if x < 0 else 1
        x = abs(x)
        result = 0
        while x // 10:
            x, part = divmod(x, 10)
            if result > UPPER_BOUND - part:
                return 0
            result += part
            if result > UPPER_BOUND / 10:
                return 0
            result *= 10

        if result > UPPER_BOUND - x:
            return 0
        result += x
        result *= sign
        return result
