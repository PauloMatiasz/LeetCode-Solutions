# Day 09
# Problem: Invert Binary Tree
# Difficulty: Medium
# Topic: Binary Tree / Recursion

# EXPLANATION:
# To invert a binary tree, we simply swap the left and right child
# of every node.
#
# We do this recursively:
# - swap left and right
# - call the function for the left subtree
# - call the function for the right subtree

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        # Swap left and right
        root.left, root.right = root.right, root.left

        # Invert subtrees
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root

