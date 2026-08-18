# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return 
        elif not list1:
            return list2
        elif not list2:
            return list1

        # so two sorted ll came 
        l1 = list1
        l2 = list2

        dummy = tail = ListNode(None)

        while l1 and l2:
            if l1 and l2 and  l1.val<l2.val:
                tail.next = l1
                l1 = l1.next
            elif l1 and l2 and l1.val>=l2.val:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
            
        if l1:
            # while l1.next:
                tail.next = l1
                tail = tail.next
                l1 = l1.next
        if l2:
            # while l2.next:
                tail.next = l2
                tail = tail.next
                l2 = l2.next
        return dummy.next


