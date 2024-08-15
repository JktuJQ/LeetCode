class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = []
        for i in range(len(s)):
            if s[i] == ")" and stack and s[stack[-1]] == "(":
                stack.pop()
                continue
            stack.append(i)
        
        if not stack:
            return len(s)

        max_length = 0
        last_index = len(s)
        while stack:
            prev_index = stack.pop()
            max_length = max(max_length, last_index - prev_index - 1)
            last_index = prev_index
        return max(max_length, last_index)
