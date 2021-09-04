class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {} 
        for i in range(len(nums)):
            hashmap[nums[i]] = i 
        
        for i in range(len(nums)):
            if target - nums[i] in hashmap and hashmap[target - nums[i]] != i:
                return [i, hashmap[target-nums[i]]]
            
    # O(N) going through the list 
    # O(N) items stored in the hash map
