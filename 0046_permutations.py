class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = [] 
        if len(nums) == 1:
            return [nums[:]]
        
        for i in range(len(nums)): #1,2,3.   #3, 2
            n = nums.pop(0) #1.  #2   #3
            perms = self.permute(nums) #2,3    #3    #2
            
            for perm in perms:
                perm.append(n) #3, 2
            result.extend(perms) #3, 2, 
            print(result)
            nums.append(n) #2
            
        return result
    
    # O(N!) time
    # O(N!) space
