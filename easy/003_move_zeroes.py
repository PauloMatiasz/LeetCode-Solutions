
# Day 03
# Problem: Move Zeroes
# Difficulty: Easy
# Topic: Two Pointers / Array

# EXPLANATION:
# We move all non-zero numbers to the front of the array
# and keep track of the position where the next non-zero
# value should be placed.
#
# After that, the remaining positions are filled with zeros.

class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        insert_pos = 0

        # Move non-zero elements forward
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[insert_pos] = nums[i]
                insert_pos += 1

        # Fill the rest with zeros
        for i in range(insert_pos, len(nums)):
            nums[i] = 0
