# Day 02
# Problem: Binary Search
# Difficulty: Easy
# Topic: Binary Search

# EXPLANATION:
# Binary Search works only on sorted arrays.
# We compare the middle element with the target.
#
# If the target is greater -> search on the right side
# If the target is smaller -> search on the left side
# If equal -> return the index

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                return mid

        return -1