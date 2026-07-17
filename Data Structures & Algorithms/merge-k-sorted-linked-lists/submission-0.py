# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq

class Solution: 
    def merge2lists(self, head1, head2):
        dummy = ListNode(0, None)
        curr = dummy
        while head1 and head2:
            if head1.val > head2.val:
                curr.next = head2
                head2 = head2.next
            else:
                curr.next = head1
                head1 = head1.next
            curr = curr.next
        if head1:
            curr.next = head1
        if head2: 
            curr.next = head2
        return dummy.next


    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None

        while len(lists) > 1:
            mergedLists = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i+1] if (i + 1) < len(lists) else None
                mergedLists.append(self.merge2lists(l1, l2))
            lists = mergedLists
        
        return lists[0]

        # n = len(lists)
        # for i in range(1,n):
        #     lists[i] = self.merge2lists(lists[i], lists[i-1])
        
        return lists[n-1]
        
