# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        leftprev = ListNode(0, head)
        curr = head 
        dummy = leftprev
        
        for i in range(left-1):
            leftprev = curr
            curr = curr.next
            
        prev = None
        for _ in range(right - left + 1):
            rightafter = curr.next
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt 
            
        leftprev.next = prev
        
        while leftprev and leftprev.next:
            leftprev = leftprev.next 
        
        leftprev.next = rightafter
        
            
        return dummy.next
    
    # O(N) time
    # O(1) space
