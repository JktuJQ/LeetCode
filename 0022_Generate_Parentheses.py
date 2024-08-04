class Solution:
    def generate(prefix: str, n: int, opened: int) -> List[str]:
        if n == 0:
            return [prefix]
        
        result = []
        if n - opened >= 2:
            result.extend(Solution.generate(prefix + "(", n - 1, opened + 1))
        if opened > 0:
           result.extend(Solution.generate(prefix + ")", n - 1, opened - 1))
        return result

    def generateParenthesis(self, n: int) -> List[str]:
        results = []
        results.extend(Solution.generate("", n * 2, 0))
        return results
