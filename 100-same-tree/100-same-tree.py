# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        arr1 = []
        arr2 = []
        self.preOrderTraversal(p, arr1)
        self.preOrderTraversal(q, arr2)
        return arr1==arr2

    def preOrderTraversal(self, node, tree):
        
        if node is not None:
            tree.append(node.val)
            if node.left:
                self.preOrderTraversal(node.left, tree)   
            elif node.left is None and node.right is not None:
                tree.append('null')
            self.preOrderTraversal(node.right, tree)
   
            
        