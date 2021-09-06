class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = ""
        self.ans = [] 
        def dfs(res, opening, closing):
            if opening == n and closing == n:
                self.ans.append(res)
                return 
            if opening != n:
                dfs(res + "(", opening + 1, closing)
            if closing != n and opening > closing:
                dfs(res + ")", opening, closing +1) 
        
        
        dfs(res, 0, 0)
        return self.ans
    
    # O(N) time
    # O(N) space
