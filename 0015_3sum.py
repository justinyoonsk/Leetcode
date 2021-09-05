class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return [] 
        
        nums.sort()
        res = [] 
        
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left = i + 1 
            right = len(nums)-1
            while left < right:
                target = nums[i] + nums[left] + nums[right]
                if target == 0:
                    if [nums[i], nums[left], nums[right]] not in res:
                        res.append([nums[i], nums[left], nums[right]])
                    left += 1 
                    right -= 1 
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1 
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1 
                elif target < 0:
                    left += 1 
                elif target > 0:
                    right -= 1 
        
        
        return res
    
    # O(N^2 + NLogN) time O(nlogn) sort so asymptotically equivalent to O(N^2)
    # O(N) 
