# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversalNode(self, root:Optional[TreeNode],resultList:Optional[List]):
        tempNode = root
        if root==None:
            return

        if tempNode.left != None:
            self.inorderTraversalNode(tempNode.left,resultList)
            
        resultList.append(tempNode.val)

        if tempNode.right != None:
            tempNode = tempNode.right
            self.inorderTraversalNode(tempNode,resultList)

    
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        self.inorderTraversalNode(root,result)
        return result
        
            
        
        
        
