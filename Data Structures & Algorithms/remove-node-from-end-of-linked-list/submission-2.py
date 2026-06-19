# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # head = [1,2,3,4], n = 2
        # ouput = [1,2,4]

        curr = head
        prev = None
        length = 0
        while curr:
            length += 1
            prev = curr
            curr = curr.next

        index_n = length - n

        curr2, prev2 = head, None
        i = 0
        while curr2:
            tmp = curr2.next

            if i == index_n:
                if i == 0:
                    return head.next
                prev2.next = tmp
                curr2.next = None
                break
            
            prev2 = curr2
            curr2 = curr2.next
            i += 1

        return head