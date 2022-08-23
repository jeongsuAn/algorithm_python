# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None : 
            return head
        tempNode = head
        nextTempNode = tempNode.next
        tempNode.next = None
        while True:
            if nextTempNode.next == None:
                nextTempNode.next = tempNode #이제 tempNode 필요 없어짐. head(tempNode) <- nextTempNode 
                return nextTempNode
            nextNextTempNode = nextTempNode.next
            nextTempNode.next = tempNode
            tempNode = nextTempNode
            nextTempNode = nextNextTempNode
