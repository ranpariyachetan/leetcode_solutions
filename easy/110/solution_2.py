# https://leetcode.com/problems/balanced-binary-tree

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

heights = {}
def isBalanced(root: Optional[TreeNode]) -> bool:
    def dfs(node):
        if not node:
            return 0

        left_height = dfs(node.left)

        if left_height == -1:
            return -1
        
        right_height = dfs(node.right)
        if right_height == -1:
            return -1
        
        return 1 + max(left_height, right_height)

    return dfs(root) != -1

input = TreeNode(3)
input.left = TreeNode(9)
input.right = TreeNode(20)
input.right.left = TreeNode(15)
input.right.right = TreeNode(7)

print(isBalanced(input))  # expected = True

input = TreeNode(1)
input.left = TreeNode(2)
input.right = TreeNode(2)
input.left.left = TreeNode(3)
input.left.right = TreeNode(3)
input.left.left.left = TreeNode(4)

print(isBalanced(input))  # expected = False

input = TreeNode(1)
input.left = TreeNode(2)
input.right = TreeNode(2)
input.left.left = TreeNode(3)
input.left.right = TreeNode(3)
input.left.left.left = TreeNode(4)
input.right.left = TreeNode(5)
input.right.right = TreeNode(5)
input.right.left.left = TreeNode(6)
input.right.left.right = TreeNode(6)

print(isBalanced(input))  # expected = True

input = TreeNode(1)
input.left = TreeNode(2)
input.right = TreeNode(2)
input.left.left = TreeNode(3)
input.right.right = TreeNode(3)
input.left.left.left = TreeNode(4)
input.right.right.right = TreeNode(4)

print(isBalanced(input))  # expected = False