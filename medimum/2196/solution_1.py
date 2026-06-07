# https://leetcode.com/problems/create-binary-tree-from-descriptions

from typing import List
from typing import Optional

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def createBinaryTree(descriptions: List[List[int]]) -> Optional[TreeNode]:

    node_map = {}
    childids = set()
    for desc in descriptions:
        childids.add(desc[1])

    root_id = -1
    for description in descriptions:
        parent = description[0]
        child = description[1]
        isLeft = bool(description[2])
        if not parent in childids:
            root_id = parent

        if not child in node_map:
            childNode = TreeNode(child)
            node_map[child] = childNode
        if not parent in node_map:
            parentNode = TreeNode(parent)
            node_map[parent] = parentNode
            
        if isLeft:
            node_map[parent].left = node_map[child]
        else:
            node_map[parent].right = node_map[child]
    return node_map[root_id]


descriptions = [[20,15,1],[20,17,0],[80,19,1],[50,20,1],[50,80,0],]

root_node = createBinaryTree(descriptions)
print(root_node.val)

descriptions = [[1,2,1],[2,3,0],[3,4,1]]
root_node = createBinaryTree(descriptions)
print(root_node.val)