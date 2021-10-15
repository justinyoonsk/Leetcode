class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0 
        right = len(nums) - 1 
        
        while left <= right:
            mid = left + (right - left) // 2
            if left == right and target > nums[left]:
                return left + 1 
            if left == right and target < nums[left]:
                return left 
            
            if nums[mid] == target:
                return mid 
            if nums[mid] > target:
                right = mid
            if nums[mid] < target:
                left = mid + 1
                
    # O(logN) time
    # O(1) space
