# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sentinel = ListNode(0)
        dummy = sentinel
        
        while l1 and l2:
            if l1.val <= l2.val:
                sentinel.next = l1
                l1 = l1.next
            else:
                sentinel.next = l2 
                l2 = l2.next
            
            sentinel = sentinel.next
            
        if not l1:
            sentinel.next = l2 
        
        if not l2:
            sentinel.next = l1 
        
        return dummy.next
    
    # O(N + M) time
    # O(1) space
