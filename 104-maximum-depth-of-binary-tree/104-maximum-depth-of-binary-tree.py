# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkDepth(self, root: Optional[TreeNode], tempDepth, result):
        thisDepth = tempDepth + 1
#        print("현재 노드 : ",root)
#        print("현재 깊이 : ",thisDepth)
#        print("result List : ",result)
#        print()
        if root.left == None and root.right == None:
            result.append(thisDepth)
        if root.left != None:
            self.checkDepth(root.left,thisDepth,result)
        if root.right != None:
            self.checkDepth(root.right,thisDepth,result)
    
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        result = []
        tempDepth = 0
        if root == None:
            return 0
        elif root.left == None and root.right == None:
            return 1
        else :
            self.checkDepth(root, tempDepth, result)
            return max(result)
            
        