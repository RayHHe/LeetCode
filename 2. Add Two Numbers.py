# No.1/2019-06-03/76 ms/13.2 MB	 

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        flag=0
        l3=ListNode(0)
        temp_node=l3
        while 1:
            val=l1.val+l2.val+flag
            flag=0
            if val>9:
                flag=1
                temp_node.val=val-10
                temp_node.next=ListNode(1)
            else:
                temp_node.val=val
            if l1.next==None and l2.next==None:
                break
            temp_node.next=ListNode(0)
            temp_node=temp_node.next
            if l1.next:
                l1=l1.next
            else:
                l1=ListNode(0)
            if l2.next:
                l2=l2.next
            else:
                l2=ListNode(0)
        return l3
