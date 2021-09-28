class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        
        dp = [0 for _ in range(target+1)] 
        dp[0] = 0 
        
        for i in range(len(dp)):
            if i > 0:
                if i in nums:
                    dp[i] = 1 
                for j in nums:
                    if i - j >= 0:
                        dp[i] += dp[i - j]
        
        print(dp)
        return dp[target]
    
    # O(T*N) time
    # O(T) space
