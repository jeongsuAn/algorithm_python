# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        linkedListLen = 1
        tempNode = head
        while tempNode.next != None:
            linkedListLen += 1
            tempNode = tempNode.next
        
        if linkedListLen % 2 == 0:
            resultNodeIdx = int(linkedListLen/2)
        else :
            resultNodeIdx = int(linkedListLen/2)
        
        resultNode = head
        for i in range(resultNodeIdx):
            resultNode = resultNode.next
        
        return resultNode
        