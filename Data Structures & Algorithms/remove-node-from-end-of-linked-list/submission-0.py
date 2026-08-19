# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # so from end remove the nth eg.n=2 
        # piche se doosri 
        # mean from the front remove k - n + 1
        # get lenth of the list in k
        k=0
        temp = head
        while temp :
            temp = temp.next
            k+=1   
        newN = k - n + 1
        if newN == 1:
            return head.next

        temp = head
        prev = None
        i = 1

        while temp:
            if i == newN:
                prev.next = temp.next
                break

            prev = temp
            temp = temp.next
            i += 1

        return head

        