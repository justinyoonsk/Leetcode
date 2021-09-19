class Solution:
    def sumOfBeauties(self, nums: List[int]) -> int:
        beauty = 0 
        min_heap = []
        max_heap = [] 
        
        for k in range(2,len(nums)):
            heappush(min_heap, nums[k])
            
            
        for i in range(len(nums)):
            first_condition = False
            if 0 < i < len(nums)-1:
                heappush(max_heap, -nums[i-1])
                if -max_heap[0] < nums[i] < min_heap[0]:
                    beauty += 2 
                    first_condition = not first_condition
                if min_heap[0] == nums[i+1]:
                    heappop(min_heap)

            
            if first_condition == False and i >= 1 and i < len(nums)-1 and nums[i-1] and nums[i+1] and nums[i-1] < nums[i] < nums[i+1]:
                beauty += 1 
            
        return beauty 
    
    # O(NLogN) time
    # O(N) space
