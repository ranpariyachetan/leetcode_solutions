# https://leetcode.com/problems/balanced-binary-tree

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

heights = {}
def isBalanced(root: Optional[TreeNode]) -> bool:
    def height(node):
        if not node:
            return 0

        if not node in heights:
            heights[node] = 1 + max(height(node.left), height(node.right))

        return heights[node]

    if not root:
        return True
    left_height = height(root.left)
    right_height = height(root.right)

    return isBalanced(root.left) and isBalanced(root.right) and abs(left_height - right_height) <= 1

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