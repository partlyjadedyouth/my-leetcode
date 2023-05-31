# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cnt = 0
        middle = head
        while head:
            cnt += 1
            if cnt % 2 == 0:
                middle = middle.next
            head = head.next
        return middle
