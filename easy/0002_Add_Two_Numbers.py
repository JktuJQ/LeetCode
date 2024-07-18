# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode()
        current = result

        carry = 0
        while l1 is not None or l2 is not None:
            current.next = ListNode()
            current = current.next

            x = 0
            if l1 is not None:
                x = l1.val
                l1 = l1.next
            
            y = 0
            if l2 is not None:
                y = l2.val
                l2 = l2.next

            carry, value = divmod(x + y + carry, 10)
            current.val = value
        if carry != 0:
            current.next = ListNode(carry)
        return result.next
