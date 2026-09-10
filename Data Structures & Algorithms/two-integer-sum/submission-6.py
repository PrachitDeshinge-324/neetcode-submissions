class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictionary = {}
        for i, num in enumerate(nums):
            if num in dictionary:
                dictionary[num].append(i)
            else:
                dictionary[num] = [i]
        ans = []
        for i,num in enumerate(nums):
            target1 = target-num
            if target1 not in dictionary:
                continue
            else:
                if num == target1:
                    if len(dictionary[num]) > 1:
                        ans.append(dictionary[num][0])
                        ans.append(dictionary[num][1])
                    else:
                        continue
                else:
                    ans.append(dictionary[num][0])
                    ans.append(dictionary[target1][0])
                return ans
        return []