# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        # brute is to have 2 array of the ll data do over that
        dummy = tail = ListNode()
        l1, l2 = list1, list2
        carry = 0
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            currSum = val1 + val2 + carry

            digit = currSum % 10
            carry = currSum // 10

            tail.next = ListNode(digit)

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            tail = tail.next
        return dummy.next
