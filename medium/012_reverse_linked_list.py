# Day 12
# Problem: Reverse Linked List
# Difficulty: Easy
# Topic: Linked List / Pointers

# EXPLANATION:
# We reverse the linked list by changing the direction
# of the pointers one by one.
#
# For each node:
# 1. Save the next node
# 2. Reverse the pointer
# 3. Move forward in the list

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previous = None
        current = head

        while current:
            next_node = current.next      # save next node
            current.next = previous       # reverse pointer
            previous = current            # move previous forward
            current = next_node           # move current forward

        return previous
    
#Comentario
