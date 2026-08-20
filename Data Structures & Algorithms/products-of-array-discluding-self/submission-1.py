class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans1 = [1]*(len(nums)+1)
        for i,val in enumerate(nums):
            ans1[i+1]=ans1[i]*val
        ans2 = [1]*(len(nums)+1)
        for i in range(len(nums)-2,-1,-1):
            ans2[i] = ans2[i+1]*nums[i+1]
        ans = [1]*len(nums)
        for i in range(len(nums)):
            ans[i] = ans1[i]*ans2[i]
        return ans