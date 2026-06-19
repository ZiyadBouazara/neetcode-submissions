# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# prev -> curr -> next
# prev <- curr <- next
#

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr:
            tmp_next = curr.next

            curr.next = prev

            prev = curr
            curr = tmp_next
        
        return prev
