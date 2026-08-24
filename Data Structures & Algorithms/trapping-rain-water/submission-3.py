class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height)-1
        maxLeft, maxRight = height[left], height[right]
        ans = 0
        while left < right:
            if maxLeft < maxRight:
                left+=1
                maxLeft = max(maxLeft,height[left])
                ans += maxLeft-height[left]
            else:
                right-=1
                maxRight = max(maxRight,height[right])
                ans += maxRight-height[right]
        return ans