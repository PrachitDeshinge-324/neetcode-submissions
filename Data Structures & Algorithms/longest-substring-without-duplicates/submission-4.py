class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        visited = set()
        l, maxlen = 0, 0

        for r in range(len(s)):
            if s[r] in visited:
                while s[r] in visited:
                    visited.remove(s[l])
                    l += 1

            visited.add(s[r])
            maxlen = max(maxlen, r - l + 1)

            # print(s[i], visited, l, r, maxlen)

        return maxlen
