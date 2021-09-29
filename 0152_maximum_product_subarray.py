class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_so_far = nums[0]
        min_so_far = nums[0]
        result = nums[0]
        
        for i in range(1,len(nums)):
            temp = max_so_far
            max_so_far = max(nums[i], max_so_far * nums[i], min_so_far * nums[i])
            min_so_far = min(nums[i], temp * nums[i], min_so_far * nums[i])
            
            result = max(result, max_so_far)
            
        return result
    
    # O(N) time
    # O(1) space
