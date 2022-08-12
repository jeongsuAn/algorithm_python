# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:    
    
    def inorderTraversal(self, tempNode: Optional[TreeNode], result:Optional[List]):
        if tempNode == None:
            return
        if tempNode.left != None:
            self.inorderTraversal(tempNode.left,result)
        if tempNode.left !=None and tempNode.right == None:
            result.append(0)
        result.append(tempNode.val)
        if tempNode.right != None:
            self.inorderTraversal(tempNode.right,result)
      
        
    def reverseInordrTraversal(self, tempNode: Optional[TreeNode],result:Optional[List]):
        if tempNode == None:
            return
        if tempNode.right != None:
            self.reverseInordrTraversal(tempNode.right,result)
        if tempNode.left == None and tempNode.right != None:
            result.append(0)
        result.append(tempNode.val)
        if tempNode.left != None:
            self.reverseInordrTraversal(tempNode.left,result)
        
        
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        leftResult = []
        rightResult = []
        
        if root==None :
            return True
        elif root.left != None and root.right == None:
            return False
        elif root.left == None and root.right != None:
            return False
        elif root.left == None and root.right == None:
            return True
        elif root.left.val != root.right.val:
            return False
        else: 
            self.inorderTraversal(root.left,leftResult)
            self.reverseInordrTraversal(root.right,rightResult)
            if leftResult == rightResult:
                print(leftResult)
                print(rightResult)
                return True
            else:
                print(leftResult)
                print(rightResult)
                return False
                
            
        