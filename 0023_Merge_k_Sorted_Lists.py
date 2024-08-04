class Solution:
    def merge_lists(self, list1, list2):
        result = ListNode()
        current = result
        
        while list1 and list2:
            if list1.val > list2.val:
                current.next = list2
                list2 = list2.next
            else:
                current.next = list1
                list1 = list1.next
            current = current.next
        
        if list1:
            current.next = list1
        else:
            current.next = list2
        return result.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]: 
        if not lists or len(lists) == 0:
            return None
        
        while len(lists) > 1:
            temp = []
            for i in range(0, len(lists), 2):
                list1 = lists[i]
                list2 = lists[i + 1] if i + 1 < len(lists) else None
                temp.append(self.merge_lists(list1, list2))
            lists = temp
        
        return lists[0]
