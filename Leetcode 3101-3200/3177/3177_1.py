# Leetcode 3177: Find the Maximum Length of a Good Subsequence II
# https://leetcode.com/problems/find-the-maximum-length-of-a-good-subsequence-ii/
# Solved on 11th of August, 2025
class Solution:
    def maximumLength(self, nums: list[int], k: int) -> int:
        """
        Finds the maximum length of a good subsequence.

        Args:
            nums (list[int]): The input list of integers.
            k (int): The maximum number of allowed differences.
        Returns:
            int: The maximum length of a good subsequence.
        """
        dpMaps = [{} for _ in range(k + 1)]
        maxLen = [0] * (k + 1)

        for num in nums:
            for j in range(k, -1, -1):
                lenSame = dpMaps[j].get(num, 0) + 1

                lenDiff = 0
                if j > 0:
                    lenDiff = maxLen[j - 1] + 1

                currentLen = max(lenSame, lenDiff)

                dpMaps[j][num] = currentLen
                maxLen[j] = max(maxLen[j], currentLen)

        return maxLen[k]