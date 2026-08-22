class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area_max = 0
        left, right = 0, len(heights)-1
        while left < right:
            l = min(heights[left],heights[right])
            b = right - left
            area_max = max(area_max,l*b)
            if heights[left]>heights[right]:
                right-=1
            else:
                left+=1
        return area_max