class Solution:
    def apply_sign(num: int, sign: int) -> int:
        if sign == -1:
            return -num
        return num

    def divide(self, dividend: int, divisor: int) -> int:
        sign = 1 if (dividend > 0) == (divisor > 0) else -1
        dividend, divisor = abs(dividend), abs(divisor)

        if divisor == 1:
            dividend = Solution.apply_sign(dividend, sign)
            if dividend > 2 ** 31 - 1:
                return 2 ** 31 - 1
            if dividend < -2 ** 31:
                return -2 ** 31
            return dividend

        quotient = 0

        while dividend >= divisor:
            k = divisor
            count = 1
            while dividend >= (k << 1):
                k <<= 1
                count <<= 1
            dividend -= k
            quotient += count
        
        quotient = Solution.apply_sign(quotient, sign)
        if quotient > 2 ** 31 - 1:
            return 2 ** 31 - 1
        if quotient < -2 ** 31:
            return -2 ** 31
        return quotient
