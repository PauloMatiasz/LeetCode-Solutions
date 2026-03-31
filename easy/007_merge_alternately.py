# Day 07
# Problem: Merge Strings Alternately
# Difficulty: Easy
# Topic: String / Two Pointers

# EXPLANATION:
# We iterate through both strings at the same time.
# At each position, we add one character from word1
# and one character from word2.
#
# If one string is longer, we append the remaining characters at the end.

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = []
        i = 0

        while i < len(word1) or i < len(word2):
            if i < len(word1):
                result.append(word1[i])

            if i < len(word2):
                result.append(word2[i])

            i += 1

        return "".join(result)