# Day 10
# Problem: Binary Tree Level Order Traversal
# Difficulty: Medium
# Topic: Binary Tree / BFS / Queue

# EXPLANATION:
# We use Breadth-First Search (BFS) to visit the tree level by level.
#
# A queue is used to store the nodes of the current level.
# For each level, we process all nodes currently in the queue
# and store their values in a list.
#
# Then we add their children to the queue for the next level.

from typing import Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> list[list[int]]:
        if not root:
            return []

        result = []
        queue = deque([root])

        while queue:
            level = []

            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(level)

        return result

