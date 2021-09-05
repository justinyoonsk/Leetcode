class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0 
        right = len(height)-1
        max_water = float("-inf")
        while left < right:
            max_water = max(min(height[left],height[right]) * (right - left), max_water)
            if height[left] < height[right]:
                left += 1 
            elif height[left] >= height[right]:
                right -= 1 
            
        return max_water
     
    # O(N) time
    # O(1) space
