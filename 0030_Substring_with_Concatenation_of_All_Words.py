class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if all(words[i] == words[i + 1] for i in range(len(words) - 1)) and \
            all(words[0][i] == words[0][i + 1] for i in range(len(words[0]) - 1)) and \
            s[0] == s[-1]:
            return list(range(len(s) - len(words) * len(words[0]) + 1))

        result = []
        word_len = len(words[0])

        i = 0
        while i <= len(s):
            start = i
            garbage = set()
            while len(words) != len(garbage):
                for current in range(len(words)):
                    if current not in garbage and s[i:i + word_len] == words[current]:
                        i += word_len
                        garbage.add(current)
                        break
                else:
                    break
            else:
                result.append(start)
            i = start + 1
        return result
