class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0
        
        hashmap = {} 
        window_start = 0 
        maxlen = float("-inf")
        
        for i in s:
            while i in hashmap:
                del hashmap[s[window_start]]
                window_start += 1 
            hashmap[i] = 1
            maxlen = max(maxlen, len(hashmap))
        
        return maxlen
    
    # O(N) time 
    # O(N) space
