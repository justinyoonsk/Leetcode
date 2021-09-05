class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        max_heap = [] 
        min_heap = [] 
        
        nums3 = [] 
        for i in nums1:
            nums3.append(i)
        for i in nums2:
            nums3.append(i)
        
        for i in nums3:
            if not max_heap or -max_heap[0] >= i:
                heappush(max_heap, -i)
            else:
                heappush(min_heap, i)
            
            if len(max_heap) > len(min_heap)+1:
                heappush(min_heap, -heappop(max_heap))
            elif len(max_heap) < len(min_heap):
                heappush(max_heap, -heappop(min_heap))
            
        if len(min_heap) == len(max_heap):    
            return (-max_heap[0] + min_heap[0])/2
        return -max_heap[0]
        
    # O(NlogN)
    # O(N)
