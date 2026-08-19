class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        for num in nums:
            counter[num] = counter.get(num, 0) + 1
        sorted_counter = dict(sorted(counter.items(),key=lambda item:item[1],reverse=True))
        ans = []
        for i in range (0,k):
            ans.append(list(sorted_counter.keys())[i])
        return ans