# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, head1: Optional[ListNode], head2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(101)
        dummy.next = None
        head = dummy
        while head1 and head2:
            if head1.val > head2.val:
                head.next = ListNode(head2.val)
                head = head.next
                head2 = head2.next
            else:
                head.next = ListNode(head1.val)
                head = head.next
                head1 = head1.next
        
        if head1:
            head.next = head1
        else:
            head.next = head2
        return dummy.next
