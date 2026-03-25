# Day 05
# Problem: Reverse Bits
# Difficulty: Easy
# Topic: Bit Manipulation

# EXPLANATION:
# We extract each bit from the number and place it
# in the reversed position.
#
# Example:
# bit at position 0 goes to position 31
# bit at position 1 goes to position 30
# ...

class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0

        for i in range(32):
            bit = (n >> i) & 1
            result |= (bit << (31 - i))

        return result