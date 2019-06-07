# No.1/2019-06-07/44 ms/13.2 MB

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1==None and l2==None: return l1
        elif l1==None: return l2
        elif l2==None: return l1
        if l1.val<=l2.val:
            head=t=l1
            l1=l1.next
        else:
            head=t=l2
            l2=l2.next
        while l1:
            if l2 == None or l1.val<=l2.val:
                t.next=l1
                l1=l1.next
            else:
                t.next=l2
                l2=l2.next
            t=t.next
        t.next=l2
        return head
            
