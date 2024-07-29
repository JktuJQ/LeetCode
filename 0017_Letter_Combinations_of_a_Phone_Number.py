class Solution:
    LETTERS = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz"
    }

    def degrade(digits: str, prefix: str = "") -> List[str]:
        if not digits:
            return [prefix]
        
        result = []
        digit = digits[0]
        for letter in Solution.LETTERS[digit]:
            result.extend(Solution.degrade(digits[1:], prefix + letter))
        return result

    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        return Solution.degrade(digits)
