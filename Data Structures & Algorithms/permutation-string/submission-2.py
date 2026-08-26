class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1has = {}
        for i in s1:
            s1has[i] = s1has.get(i, 0) + 1

        left = 0
        right = len(s1)

        while right <= len(s2):
            temp = s1has.copy()

            for i in range(left, right):
                if s2[i] not in temp or temp[s2[i]] == 0:
                    break

                temp[s2[i]] -= 1
            else:
                return True

            left += 1
            right += 1

        return False
