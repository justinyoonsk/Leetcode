# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        sentinel = ListNode(0)
        dummy = sentinel
        heap = [] 
        
        for l in lists:
            while l:
                heappush(heap, l.val)
                l = l.next 
        
        while heap:
            sentinel.next = ListNode(heappop(heap))
            sentinel = sentinel.next
        
        return dummy.next
    
    # O(NLogK)
    # O(N)
