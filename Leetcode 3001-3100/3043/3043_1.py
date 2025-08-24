# Leetcode 3043: Find the Length of the Longest Common Prefix
# https://leetcode.com/problems/find-the-length-of-the-longest-common-prefix/
# Resolved on 24th of August, 2025
class Solution:
    def longestCommonPrefix(self, arr1: list[int], arr2: list[int]) -> int:
        """
        Finds the length of the longest common prefix between numbers in two arrays.

        Args:
            arr1: A list of integers.
            arr2: A list of integers.

        Returns: The length of the longest common prefix.
        """
        if len(arr1) > len(arr2):
            arr1, arr2 = arr2, arr1

        prefixSet = set()
        for num in arr1:
            currentNum = num
            while currentNum > 0:
                prefixSet.add(currentNum)
                currentNum //= 10

        maxLength = 0
        for num in arr2:
            currentNum = num
            numStr = str(num)
            currentLength = len(numStr)

            while currentLength > maxLength:
                if currentNum in prefixSet:
                    maxLength = currentLength
                    break

                currentNum //= 10
                currentLength -= 1

        return maxLength