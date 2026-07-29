# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        if not head or left == right:
            return head
        
        dummy = ListNode(0)
        dummy.next = head

        beforeRev = dummy
        for _ in range(left-1):
            beforeRev = beforeRev.next

        curr = beforeRev.next
        prev = None
        supTail = curr
        for i in range(left, right+1):
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        beforeRev.next = prev
        supTail.next = curr
    
        return dummy.next



