class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 1:
            return head

        result = ListNode()
        result.next = start = last = head
        connection = result

        while True:
            i = 0
            while last and i < k:
                last = last.next
                i += 1
            
            if i == k:
                swap_left, swap_right = last, start
                for _ in range(k):
                    swap_right.next, swap_right, swap_left = swap_left, swap_right.next, swap_right
                
                connection.next, connection, start = swap_left, start, last
            else:
                return result.next
