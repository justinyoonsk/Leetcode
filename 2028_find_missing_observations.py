class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        m = len(rolls)
        nTotal = (mean * (n + m)) - sum(rolls)
        
        if nTotal < n or nTotal > n * 6:
            return [] 
        
        res = [] 
        while nTotal:
            res.append(min(nTotal - n + 1, 6))
            nTotal = nTotal - min(nTotal - n + 1, 6)
            n -= 1
        
        return res
            
    # O(N) time
    # O(N) space
