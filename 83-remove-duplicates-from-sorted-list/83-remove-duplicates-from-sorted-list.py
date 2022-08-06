# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tempNode = head
        if tempNode==None:
            return head
        while tempNode.next != None and tempNode.next.next != None:
            if tempNode.val == tempNode.next.val:
                if tempNode.next.next == None:
                    break
                tempNode.next = tempNode.next.next
                continue
            if tempNode.next.next!=None:
                tempNode = tempNode.next
        if tempNode.next !=None and tempNode.val == tempNode.next.val:
            tempNode.next = None

        return head