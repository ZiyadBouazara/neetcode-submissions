# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        curr2 = slow.next
        slow.next = None
        prev = None

        while curr2:
            tmp = curr2.next

            curr2.next = prev
            prev = curr2
            curr2 = tmp

        head1, head2 = head, prev

        while head2:
            next1 = head1.next
            next2 = head2.next

            head1.next = head2
            head2.next = next1

            head1, head2 = next1, next2

