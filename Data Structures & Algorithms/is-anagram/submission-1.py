class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dictionary = {}
        for i in s:
            dictionary[i] = dictionary.get(i,0) + 1
        for i in t:
            if i not in dictionary or dictionary[i] < 1:
                return False
            dictionary[i]-=1
        return True