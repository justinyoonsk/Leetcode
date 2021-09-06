class Solution:
    def isValid(self, s: str) -> bool:
        opening = ["(", "{", "["]
        closing = [")", "}", "]"]
        
        stack = [] 
        
        for i in s:
            if i in opening:
                stack.append(i)
            elif i in closing and stack == []:
                return False
            elif i in closing and opening.index(stack[-1]) == closing.index(i):
                stack.pop()
            else:
                return False
        
        if stack == []:
            return True
        return False
    
    # O(N) string one a time into stack
    # O(N) pushing into stack
            
