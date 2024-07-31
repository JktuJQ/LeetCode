class Solution:
    def isValid(self, s: str) -> bool:
        corresponding = {")": "(", "]": "[", "}": "{"}
        
        parentheses = []
        for symbol in s:
            if symbol in corresponding.values():
                parentheses.append(symbol)
            elif len(parentheses) == 0 or parentheses.pop() != corresponding[symbol]:
                return False
        return not parentheses
