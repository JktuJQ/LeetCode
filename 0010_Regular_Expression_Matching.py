class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        data = [[False for _ in range(len(p) + 1)] for _ in range(len(s) + 1)]
        data[0][0] = True

        for p_row in range(1, len(p) + 1):
            if p[p_row - 1] == "*":
                data[0][p_row] = data[0][p_row - 2]

        for s_row in range(1, len(s) + 1):
            for p_row in range(1, len(p) + 1):
                if p[p_row - 1] in (s[s_row - 1], "."):
                    data[s_row][p_row] = data[s_row - 1][p_row - 1]
                elif p[p_row - 1] == "*":
                    data[s_row][p_row] = data[s_row][p_row - 2]
                    if p[p_row - 2] in (s[s_row - 1], "."):
                        data[s_row][p_row] = (
                            data[s_row][p_row] or data[s_row - 1][p_row]
                        )

        return data[len(s)][len(p)]
