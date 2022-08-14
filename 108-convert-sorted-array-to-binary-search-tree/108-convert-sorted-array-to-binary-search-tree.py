# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addMidNode(self, nums: List[int], node: Optional[TreeNode]):
        # print(node)
        # print(nums)
        numsLen = len(nums)
        if numsLen == 0:
            return
        elif numsLen == 1:
            node.val = nums[0]
        else:
            midIndex = int(numsLen/2)
            node.val = nums[midIndex]
            if midIndex-1>=0:
                node.left = TreeNode()
                # print("midIndex-1 : ",midIndex-1)
                # print("self.addMidNode(nums[0:midIndex-1], node.left)")
                self.addMidNode(nums[0:midIndex], node.left)
            if numsLen-1 - (midIndex+1) >= 0:
                node.right = TreeNode()
                # print("numsLen-1 : ",numsLen-1)
                # print("nums[midIndex:numsLen-1], node.right")
                self.addMidNode(nums[midIndex+1:numsLen], node.right)

    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        rootNode = TreeNode()
        self.addMidNode(nums,rootNode)
        return rootNode