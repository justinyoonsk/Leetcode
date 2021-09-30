class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = deque()
        res = [] 
        left = 0 
        for i in range(len(nums)):
            if i < k:
                while queue and nums[i] > queue[-1]:
                    queue.pop()
                queue.append(nums[i])
            else:
                res.append(queue[0])
                while queue and nums[i] > queue[-1]:
                    queue.pop()
                queue.append(nums[i])
                
                if nums[left] == queue[0]:
                    queue.popleft()
                left += 1 
                
        res.append(queue[0])
            
        return res
    
    # O(N) time 
    # O(N) space
