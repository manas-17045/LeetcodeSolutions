# Leetcode 3489: Zero Array Transformation IV
# https://leetcode.com/problems/zero-array-transformation-iv/
# Solved on 21st of November, 2025
class Solution:
    def minZeroArray(self, nums: list[int], queries: list[list[int]]) -> int:
        """
        Determines the minimum number of queries required to transform all elements of `nums` to zero.

        Args:
            nums: A list of integers representing the initial array.
            queries: A list of queries, where each query is [l, r, val].

        Returns:
            The minimum number of queries needed to make all elements zero, or -1 if it's not possible.
        """
        n = len(nums)
        reachable = [1] * n
        isSolved = [False] * n
        solvedCount = 0

        for i in range(n):
            if nums[i] == 0:
                isSolved[i] = True
                solvedCount += 1

        if solvedCount == n:
            return 0

        for k in range(len(queries)):
            l, r, val = queries[k]
            for i in range(l, r + 1):
                if isSolved[i]:
                    continue

                reachable[i] |= (reachable[i] << val)

                if (reachable[i] >> nums[i]) & 1:
                    isSolved[i] = True
                    solvedCount += 1

            if solvedCount == n:
                return k + 1

        return -1