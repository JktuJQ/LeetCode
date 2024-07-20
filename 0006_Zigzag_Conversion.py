class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
        
        rows = [[] for row in range(numRows)]

        index = 0
        direction = -1

        for letter in s:
            rows[index].append(letter)
            if index == 0:
                direction = 1
            elif index == numRows - 1:
                direction = -1
            index += direction

        for i in range(numRows):
            rows[i] = "".join(rows[i])

        return "".join(rows)
