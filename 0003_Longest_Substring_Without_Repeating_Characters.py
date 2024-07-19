class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        start, end = 0, 0
        seen = dict()

        while end < len(s):
            max_length = max(max_length, len(seen))
            if s[end] not in seen:
                seen[s[end]] = 1
                end += 1
            else:
                seen[s[start]] -= 1
                if seen[s[start]] <= 0:
                    del seen[s[start]]
                if s[end] not in seen:
                    seen[s[end]] = 1
                else:
                    seen[s[end]] += 1
                start += 1
                end += 1
                if end >= len(s):
                    break
                while len(seen.keys()) != end - start:
                    seen[s[start]] -= 1
                    if seen[s[start]] <= 0:
                        del seen[s[start]]
                    if s[end] not in seen:
                        seen[s[end]] = 1
                    else:
                        seen[s[end]] += 1
                    start += 1
                    end += 1
                    if end >= len(s):
                        break

        return max(max_length, len(seen))
