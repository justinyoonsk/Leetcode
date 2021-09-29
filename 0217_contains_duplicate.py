class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashmap = {} 
        for i in nums:
            if i in hashmap:
                return True
            hashmap[i] = 0
        
        return False
        
    # O(N) time
    # O(N) space
