class Solution:
    @staticmethod
    def choose_best(data: List[Tuple[str, int]], num: int) -> Tuple[str, int]:
        choice = len(data) - 1
        while data[choice][1] > num:
            choice -= 1
        return data[choice]

    def intToRoman(self, num: int) -> str:
        symbols = (
            ("I", 1),
            ("V", 5),
            ("X", 10),
            ("L", 50),
            ("C", 100),
            ("D", 500),
            ("M", 1000),
        )
        subtractive = (
            ("IV", 4),
            ("IX", 9),
            ("XL", 40),
            ("XC", 90),
            ("CD", 400),
            ("CM", 900),
        )

        result = ""
        num = str(num)
        while num != "0":
            if num[0] not in ("4", "9"):
                letter, n = Solution.choose_best(symbols, int(num))
            else:
                letter, n = Solution.choose_best(subtractive, int(num))
            num = str(int(num) - n)
            result = result + letter

        return result
