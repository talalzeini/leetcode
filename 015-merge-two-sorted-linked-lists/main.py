class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        # Time Complexity: O(n + m) => O(n)
        # Space Complexity: O(1)
        
        res = dummy = ListNode()

        while list1 and list2:
            if list1.val > list2.val:
                res.next = list2
                list2 = list2.next
            else:
                res.next = list1
                list1 = list1.next
            res = res.next

        res.next = list1 or list2
        return dummy.next
