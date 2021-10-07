class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        temp = [] 
        res = [[]] 
        def backtrack(i, temp):
            if i == len(nums):
                return
            for n in range(i, len(nums)):
                if n > i and nums[n] == nums[n-1]:
                    continue
                temp.append(nums[n])
                res.append(temp[:])
                backtrack(n+1, temp)
                temp.pop()
                
        backtrack(0, temp)
        return res
    
    # O(N *2^N) time
    # O(N) space
