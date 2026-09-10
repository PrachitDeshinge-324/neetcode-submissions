class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        duplicate = {}
        for i in nums:
            duplicate[i] = duplicate.get(i,0) + 1
            if duplicate[i] > 1:
                return True
        return False