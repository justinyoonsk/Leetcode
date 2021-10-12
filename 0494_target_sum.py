class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {} 
        def dfs(i, total_sum):
            if (i, total_sum) in dp:
                return dp[(i, total_sum)]
            
            if i == len(nums) and total_sum == target:
                return 1
            if i == len(nums):
                return 0
                
            ans = dfs(i + 1, total_sum + nums[i]) + dfs(i + 1, total_sum - nums[i])
            dp[(i, total_sum)] = ans
            
            return ans
            
        return dfs(0, 0)
        
    # O(2 ^ n) time
    # O(2 ^ n) space
