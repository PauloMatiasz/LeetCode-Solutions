# Day 04
# Problem: Single Number
# Difficulty: Easy
# Topic: Bit Manipulation

# EXPLANATION:
# Every number appears twice except one.
# Using XOR we can eliminate the repeated numbers:
#
# a ^ a = 0
# a ^ 0 = a
#
# So when we XOR all numbers together,
# the repeated ones cancel out and only the unique number remains.

class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        result = 0

        for num in nums:
            result ^= num

        return result