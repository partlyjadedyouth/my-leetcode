from typing import Optional


#  Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = ""
        while l1:
            num1 = str(l1.val) + num1
            l1 = l1.next

        num2 = ""
        while l2:
            num2 = str(l2.val) + num2
            l2 = l2.next

        num3 = list(str(int(num1) + int(num2)))
        num3.reverse()

        l3 = ListNode(num3[0])
        temp = l3
        for i in range(1, len(num3)):
            insert_node = ListNode(num3[i])
            temp.next = insert_node
            temp = temp.next

        return l3
