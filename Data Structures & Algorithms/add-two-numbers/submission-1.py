# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        head = ListNode()
        temp = head
        while l1 or l2:
            if not l1:
                sumVal = l2.val + carry
                l2 = l2.next
            elif not l2:
                sumVal = l1.val + carry
                l1 = l1.next
            else:
                sumVal = l1.val + l2.val + carry
                l1 = l1.next
                l2 = l2.next
            curr = ListNode()
            carry = 0
            if sumVal > 9:
                sumVal = sumVal - 10
                carry = 1 
            curr.val = sumVal
            temp.next = curr
            temp = curr
            

        if carry == 1:
            curr = ListNode(1)
            temp.next = curr
        return head.next