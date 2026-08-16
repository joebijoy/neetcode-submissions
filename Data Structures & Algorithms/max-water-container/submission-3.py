class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        max_height = 0
        while l < r:
            dist = r-l
            height = min(heights[l],heights[r]) * dist
            max_height = max(height,max_height)
            if heights[l] < heights[r]:
                l+=1
            else:
                r-=1
        
        return max_height
        