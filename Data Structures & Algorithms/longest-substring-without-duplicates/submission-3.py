class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        visited = set()
        l, r, maxlen = 0, 0, 0

        for i in range(len(s)):
            if s[i] in visited:
                while s[i] in visited:
                    visited.remove(s[l])
                    l += 1

            visited.add(s[i])
            r += 1
            maxlen = max(maxlen, r - l)

            # print(s[i], visited, l, r, maxlen)

        return maxlen
