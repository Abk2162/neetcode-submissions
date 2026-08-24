# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp = head
        count = 0
        while temp:
            count += 1
            temp = temp.next 
        delPlace = count - n
        if delPlace == 0:
            return head.next
        curr = head
        prev = head
        for i in range(delPlace):
            prev = curr
            curr = curr.next
        future = curr.next
        prev.next = future
        return head

            
        