class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [] 
        temp = [] 
        def backtrack(i, temp):
            if i == len(nums):
                res.append(temp)
                return
            dummy = temp.copy()
            temp.append(nums[i])
            
            backtrack(i+1, temp)
            backtrack(i+1, dummy)
            
        backtrack(0, temp)
        
        return res
    
    # O(N * 2^N) time
    # O(N) space
