class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0 
        
        for i in range(len(haystack)):
            if haystack[i] == needle[0] and haystack[i:i+len(needle)] == needle:
                return i 
        
        return -1 
                
    # O(N*h) time
    # O(1) space
