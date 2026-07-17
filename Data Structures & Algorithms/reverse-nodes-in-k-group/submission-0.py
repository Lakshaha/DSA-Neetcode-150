# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        groupPrev = dummy

        while True:
            knode = groupPrev
            for _ in range(k):
                knode = knode.next
                if not knode:
                    return dummy.next

            groupNext = knode.next #the next set
            prev = groupNext
            curr = groupPrev.next

            for _ in range(k):
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            
            newgroup = groupPrev.next
            groupPrev.next = knode

            groupPrev = newgroup
        
        return dummy.next
            


