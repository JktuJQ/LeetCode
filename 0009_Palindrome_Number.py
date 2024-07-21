class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        top = 1
        while x // top:
            top *= 10
        top //= 10

        while x:
            first = x // top
            last = x % 10
            if first != last:
                return False
            
            x -= x // top * top
            x //= 10
            top //= 100
        
        return True
