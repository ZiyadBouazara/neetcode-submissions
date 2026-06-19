# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second = slow.next
        curr = second
        prev = None
        slow.next = None
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        dummy = head
        while prev:
            nxt1 = dummy.next
            nxt2 = prev.next

            dummy.next = prev
            prev.next = nxt1

            dummy = nxt1
            prev = nxt2



        


        

        