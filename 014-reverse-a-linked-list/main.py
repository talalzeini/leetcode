# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # Time Complexity: O(n)
        # Space Complexity: O(1)

        prev, current = None, head

        while current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        # eventually prev become the head
        return prev