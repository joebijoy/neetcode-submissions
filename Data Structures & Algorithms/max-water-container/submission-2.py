class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        output = 0
        while left < right:
            width = right - left
            if heights[left] < heights[right]:
                if heights[left] * width > output:
                    output = heights[left] * width
                left += 1
            else:
                if heights[right] * width > output:
                    output = heights[right] * width
                right -= 1
        return output
            
