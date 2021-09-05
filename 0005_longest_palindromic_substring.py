class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_len = float("-inf")
        for i in range(len(s)):
            left = i 
            right = i 
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if max(max_len, right - left) > max_len:
                    max_len = right - left 
                    max_string = s[left:right+1]
                    
                left -= 1 
                right += 1 

        for i in range(len(s)):
            left = i 
            right = i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if max(max_len, right - left) > max_len:
                    max_len = right - left 
                    max_string = s[left:right+1]
                left -= 1 
                right += 1 
                
        return max_string
    
    # O(N^2) time
    # O(1) space
