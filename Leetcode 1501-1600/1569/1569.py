# Leetcode 1569: Number of Ways to Reorder Array to Get Same BST
# https://leetcode.com/problems/number-of-ways-to-reorder-array-to-get-same-bst/
# Solved on 22nd of October, 2025
class Solution:
    def numOfWays(self, nums: list[int]) -> int:
        """
        Calculates the number of ways to reorder the given array `nums` such that the resulting Binary Search Tree (BST)
        is the same as the BST formed by inserting elements of `nums` in their original order.
        :param nums: A list of unique integers representing the array.
        :return: The number of ways to reorder the array, modulo 10^9 + 7.
        """
        MOD = 1_000_000_007
        n = len(nums)

        combinationsTable = [[0] * (n + 1) for _ in range(n + 1)]

        for i in range(n + 1):
            combinationsTable[i][0] = 1
            if i > 0:
                combinationsTable[i][i] = 1

            for j in range(1, i):
                combinationsTable[i][j] = (combinationsTable[i - 1][j - 1] + combinationsTable[i - 1][j]) % MOD

        def countWays(arr: list[int]) -> int:

            m = len(arr)
            if m <= 2:
                return 1

            rootVal = arr[0]
            leftSubsequence = []
            rightSubsequence = []

            for val in arr[1:]:
                if val < rootVal:
                    leftSubsequence.append(val)
                else:
                    rightSubsequence.append(val)

            waysLeft = countWays(leftSubsequence)
            waysRight = countWays(rightSubsequence)

            lenLeft = len(leftSubsequence)
            lenRight = len(rightSubsequence)

            waysToInterleave = combinationsTable[lenLeft + lenRight][lenLeft]

            result = (waysLeft * waysRight) % MOD
            result = (result * waysToInterleave) % MOD

            return result

        totalWays = countWays(nums)
        return (totalWays - 1 + MOD) % MOD