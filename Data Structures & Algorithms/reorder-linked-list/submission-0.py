# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        def reverseLL(node):
            if node == None or node.next == None:
                return node
            prev = None
            curr = node
            while curr:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            return prev

        # reach milddle
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Split into two lists
        second = slow.next
        slow.next = None

        # Reverse second half
        rev = reverseLL(second)

        curr = head
        while rev != None:

            currNxt = curr.next
            curr.next = rev

            revNxt = rev.next
            rev.next = currNxt

            curr = currNxt
            rev = revNxt
