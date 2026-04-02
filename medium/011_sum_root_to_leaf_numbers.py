# Day 11
# Problem: Sum Root to Leaf Numbers
# Difficulty: Medium
# Topic: Binary Tree / DFS / Recursion

# EXPLANATION:
# We traverse the tree using DFS.
# While going down the tree, we build a number using the digits
# from the nodes.
#
# When we reach a leaf node, we convert the path into a number
# and return it.
#
# The final result is the sum of all root-to-leaf numbers.

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(node, current_number):
            if not node:
                return 0

            # Build the number
            current_number = current_number * 10 + node.val

            # If it's a leaf node, return the number
            if not node.left and not node.right:
                return current_number

            # Continue DFS
            return dfs(node.left, current_number) + dfs(node.right, current_number)

        return dfs(root, 0)