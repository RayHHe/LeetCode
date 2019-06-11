# No.1/2019-06-11/72 ms/17.3 MB

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        mergelist=[]
        for l in lists:
            while l:
                mergelist.append(l.val)
                l=l.next
        head=t=ListNode(0)
        mergelist.sort()
        for n in mergelist:
            t.next=ListNode(n)
            t=t.next
        return head.next
