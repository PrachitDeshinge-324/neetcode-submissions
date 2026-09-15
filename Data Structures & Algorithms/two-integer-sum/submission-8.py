class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict1 = {}
        for i,num in enumerate(nums):
            new = target - num
            if new in dict1:
                return [dict1[new],i]
            dict1[num] = i
        return []