#No.1/2019-06-11/36 ms/13 MB

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head==None or head.next==None: return head
        tail=head
        head=head.next
        tail.next=head.next
        head.next=tail
        while tail.next and tail.next.next:
            temp = tail.next.next
            tail.next.next=temp.next
            temp.next=tail.next
            tail.next=temp
            tail=temp.next
        return head
