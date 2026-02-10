# https://leetcode.com/problems/balance-a-binary-search-tree

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def balancesBST(root: TreeNode) -> Optional[TreeNode]:
    values = []
    
    def inorder_traversal(node):
        if not node:
            return
        
        inorder_traversal(node.left)
        values.append(node.val)
        inorder_traversal(node.right)
    
    inorder_traversal(root)
    
    def build_balanced_bst(left, right):
        if left > right:
            return None
        
        mid = (left + right) // 2
        node = TreeNode(values[mid])
        node.left = build_balanced_bst(left, mid - 1)
        node.right = build_balanced_bst(mid + 1, right)
        
        return node
    
    return build_balanced_bst(0, len(values) - 1)


input = TreeNode(1)
input.right = TreeNode(2)
input.right.right = TreeNode(3)
input.right.right.right = TreeNode(4)

output = balancesBST(input)
def print_inorder(node):
    if not node:
        return
    print_inorder(node.left)
    print(node.val, end=' ')
    print_inorder(node.right)

print_inorder(output)  # expected = 2 1 3 4