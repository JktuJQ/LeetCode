class Solution:
    
    @staticmethod
    def search_for_palindrome_length(left: int, right: int, s: str) -> int:
        l, r = left, right
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return r - l - 1

    def longestPalindrome(self, s: str) -> str:
        start, end = 0, 0

        for i in range(len(s)):
            len1 = Solution.search_for_palindrome_length(i, i, s)
            len2 = Solution.search_for_palindrome_length(i, i + 1, s)

            max_diff = max(len1, len2)
            if max_diff > end - start + 1:
                start, end = i - (max_diff - 1) // 2, i + max_diff // 2
        
        return s[start:end + 1]
