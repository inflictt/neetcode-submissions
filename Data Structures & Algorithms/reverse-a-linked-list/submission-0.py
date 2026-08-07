# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tmp=head
        prev=None
        while tmp:
            move=tmp.next
            tmp.next=prev
            prev=tmp
            tmp=move
        return prev