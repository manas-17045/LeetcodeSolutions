# Leetcode 3043: Find the Length of the Longest Common Prefix
# https://leetcode.com/problems/find-the-length-of-the-longest-common-prefix/
# Solved on 24th of August, 2025
class Solution:
    def longestCommonPrefix(self, arr1: list[int], arr2: list[int]) -> int:
        """
        Finds the length of the longest common prefix among numbers in two arrays.

        Args:
            arr1 (list[int]): The first list of integers.
            arr2 (list[int]): The second list of integers.

        Returns:
            int: The length of the longest common prefix.
        """
        # Build prefixes from the smaller array to save memory
        if len(arr1) > len(arr2):
            arr1, arr2 = arr2, arr1

        prefixes = set()
        for num in arr1:
            s = str(num)
            p = 0
            for ch in s:
                p = p * 10 + (ord(ch) - 48)  # faster than int(ch)
                prefixes.add(p)

        max_len = 0
        for num in arr2:
            s = str(num)
            p = 0
            # Build prefixes left-to-right and check membership
            for i, ch in enumerate(s, start=1):
                p = p * 10 + (ord(ch) - 48)
                if p in prefixes and i > max_len:
                    max_len = i

        return max_len