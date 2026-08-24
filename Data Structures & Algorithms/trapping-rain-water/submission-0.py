class Solution:
    def trap(self, height: List[int]) -> int:
        max_left, max_right = [0]*len(height), [0]*len(height)
        ans = 0
        for i in range(1,len(height)):
            max_left[i] = max(height[i-1],max_left[i-1])
        for i in range(len(height)-1,0,-1):
            max_right[i-1] = max(height[i],max_right[i])
        for i in range(len(height)-1):
            temp = min(max_right[i],max_left[i]) - height[i]
            if temp > 0:
                ans+=temp

        return ans