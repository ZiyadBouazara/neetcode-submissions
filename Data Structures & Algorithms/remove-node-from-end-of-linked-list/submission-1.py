# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp = head
        length = 0
        while temp:
            length += 1
            temp = temp.next
            
        target_pos = length - n
        if target_pos == 0:
            return head.next

        prev = None
        curr = head
        pos = 0
        while curr:
            if pos == target_pos:
                # delete the current node
                nxt =  curr.next
                prev.next = nxt
                break
            else:
                tmp = curr.next
                prev = curr
                curr = tmp
                pos += 1

        return head