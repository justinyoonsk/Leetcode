class Solution:
    def maxLength(self, arr: List[str]) -> int:
        
        charset = set()
        def overlap(charset, s):
            prev = set()
            for c in s:
                if c in charset or c in prev:
                    return True
            return False
        
        def backtrack(i):
            if i == len(arr):
                return len(charset) 
            res = 0 
            if not overlap(charset, arr[i]):
                for c in arr[i]:
                    charset.add(c)
                res = backtrack(i + 1)
                for c in arr[i]:
                    charset.remove(c)
                    
            return max(res, backtrack(i + 1))
            
        return backtrack(0)
            
    # O(2^N) time
    # O(N) space
