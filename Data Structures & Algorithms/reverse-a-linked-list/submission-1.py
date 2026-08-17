# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # brute pull data from the ll and srtor ein arr reverse it and then runn temp node and join all and return 
        # ll approahcc
        # using the curr prev and next idea
        prev = None #none
        curr =head #at 0
         #at 1
        while curr : #or xurr i dont knw
            nxt = curr.next
            curr.next = prev 
            prev = curr
            curr = nxt 
            
        return prev