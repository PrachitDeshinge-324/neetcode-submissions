class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictionary = {}
        for i, num in enumerate(nums):
            need = target - num
            if need in dictionary:
                return [dictionary[need],i]
            else:
                dictionary[num] = i
        return []