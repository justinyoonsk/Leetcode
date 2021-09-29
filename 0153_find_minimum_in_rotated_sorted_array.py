class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0 
        right = len(nums)-1
        mid = (left + right)//2
        
        while nums[left] > nums[right]:
            mid = (left+right)//2
            
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
                
        return nums[left]
    
    # O(logN) time
    # O(1) space
