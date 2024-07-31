class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        result = head
        
        previous = head
        current = head
        for _ in range(n):
            current = current.next
        if current is None:
            return result.next
        while current.next is not None:
            previous = previous.next
            current = current.next
        previous.next = previous.next.next

        return result
