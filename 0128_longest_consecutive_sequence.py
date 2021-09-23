class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        max_length = 0
        
        for n in nums:
            if (n-1) not in nums_set:
                length = 0 
                while (n+length) in nums_set:
                    length += 1
                max_length = max(max_length, length)
                
        return max_length
    
    # O(N) time
    # O(N) space
