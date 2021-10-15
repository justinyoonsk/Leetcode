class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        temp = [] 
        for i in nums:
            if i != 0:
                temp.append(i)
                
        for j in range(len(nums) - len(temp)):
            temp.append(0)
            
        nums[:] = temp
    
    # O(N) time
    # O(N) space 
