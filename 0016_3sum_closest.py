class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        print(nums)
        smallest_diff = float("inf")
        
        for i in range(len(nums)):
            left = i + 1
            right = len(nums) - 1 
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                target_diff = target - current_sum 
                if target_diff == 0:
                    return current_sum 
                if abs(target_diff) < abs(smallest_diff):
                    smallest_diff = target_diff
                    
                if target_diff > 0:
                    left += 1
                else:
                    right -= 1 
        return target - smallest_diff
                    
    # O(N^2)
    # O(logn) 
