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
        stack = []
        temp = head
        # put all in stack
        while temp:
            stack.append(temp)
            temp = temp.next
        # so
        curr = head
        for _ in range(len(stack) // 2): #do for only the second half 
            topNode = stack.pop()  # give me the top node in reverse order we are going
            currNext = curr.next
            curr.next = topNode
            topNode.next = currNext
            curr = currNext
        curr.next = None
