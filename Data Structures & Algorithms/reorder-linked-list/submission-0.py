# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #get the middle
        if not head:
            return None
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        head1 = head
        head2 = slow.next
        #reverse head
        curr = head2
        prev = None
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        head2 = prev
        slow.next = None
        dummy = ListNode(0)
        
        while head1 and head2:
            curr = ListNode(head2.val)
            curr.next = head1.next
            head1.next = curr
            head1 = head1.next.next
            head2 = head2.next
        
