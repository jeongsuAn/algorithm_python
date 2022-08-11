# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelorderCheck(self, tempP: Optional[TreeNode], tempQ: Optional[TreeNode] )->bool:
        print("tempP = ",tempP)
        print("tempQ = ",tempQ)
        if self.thisNodeExistCheck(tempP,tempQ) == False:
            return False
            
        if tempP.val == tempQ.val:
            if tempP.left == None:
                if self.leftNodeExistCheck(tempP,tempQ) == False:
                    return False
            else:
                if self.levelorderCheck(tempP.left, tempQ.left) == False:
                    return False
            if tempP.right == None:
                if self.rightNodeExistCheck(tempP,tempQ) == False:
                    return False
            else:
                if self.levelorderCheck(tempP.right, tempQ.right) == False:
                    return False
        else : 
            return False
        return True
    
    def thisNodeExistCheck(self, p: Optional[TreeNode], q: Optional[TreeNode])->bool:
        if p ==None :
            if q ==None:
                return True
            else : 
                return False
        elif q == None:
            if p ==None:
                return True
            else :
                return False
    
    def leftNodeExistCheck(self, p: Optional[TreeNode], q: Optional[TreeNode])->bool:
        if p.left==None :
            if q.left==None:
                return True
            else : 
                return False
            
    def rightNodeExistCheck(self, p: Optional[TreeNode], q: Optional[TreeNode])->bool:    
        if q.right == None :
            if p.right==None:
                return True
            else :
                return False
    
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p ==None :
            if q ==None:
                return True
            else : 
                return False
        elif q == None:
            if p ==None:
                return True
            else :
                return False
        return self.levelorderCheck(p,q) and self.levelorderCheck(q,p)