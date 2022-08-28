# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nodeList = []
        tempNode = head
        if tempNode == None:
            return None
        while tempNode.next != None:
            if tempNode in nodeList:
                return tempNode
            else:
                nodeList.append(tempNode)
                tempNode = tempNode.next
                
        return None