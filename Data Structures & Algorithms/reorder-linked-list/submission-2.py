# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # head = [2,4,6,8,10]
        # [2,4,6] 
        # [10,8]
        # res = [2, 10, 4, 8, 6]
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        curr = slow.next
        slow.next = None

        # reverse tail2
        prev = None
        while curr:
            tmp = curr.next
            curr.next = prev

            prev = curr
            curr = tmp
        # prev is now the new wanted tail

        # reorder the two lists together
        tail1, tail2 = head, prev
        while tail2:
            tmp1, tmp2 = tail1.next, tail2.next
            
            tail1.next = tail2
            tail2.next = tmp1

            tail1, tail2 = tmp1, tmp2


