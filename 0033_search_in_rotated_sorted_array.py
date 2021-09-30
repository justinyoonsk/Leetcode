class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0 
        right = len(nums)-1
        
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if left == right:
                return -1 
            
            if nums[mid] > nums[right] and target < nums[mid] and target >= nums[left]:
                right = mid - 1 
            elif nums[mid] > nums[right] and target < nums[mid] and target < nums[left]:
                left = mid + 1
            elif nums[mid] > nums[right] and target > nums[mid]:
                left = mid + 1 
                
            elif nums[mid] < nums[right] and target > nums[mid] and target <= nums[right]:
                left = mid + 1 
            elif nums[mid] < nums[right] and target > nums[mid] and target > nums[right]:
                right = mid - 1
                
            elif nums[mid] < nums[right] and target < nums[mid]:
                right = mid - 1 

        return -1
                
    # O(logN) time
    # O(1) space
