# No.1/2019-06-06/28 ms/13.2 MB

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        l=[]
        if head.next:
            while head:
                l.append(head)
                head=head.next
            if n==1:
                l[-2].next= None
            elif n==len(l):
                return l[1]
            else:
                l[-n-1].next=l[-n+1]
            return l[0]
        else:
            return None
