# Leetcode 3277: Maximum XOR Score Subarray Queries
# https://leetcode.com/problems/maximum-xor-score-subarray-queries/
# Solved on 23rd of July, 2025
class Solution:
    def maximumSubarrayXor(self, nums: list[int], queries: list[list[int]]) -> list[int]:
        """
        Calculates the maximum XOR score for subarrays specified by queries.

        Args:
            nums (list[int]): The input array of integers.
            queries (list[list[int]]): A list of queries, where each query is [left, right] representing a subarray.
        Returns:
            list[int]: A list of maximum XOR scores for each query.
        """
        numElements = len(nums)
        if numElements == 0:
            return []

        xorScores = [[0] * numElements for _ in range(numElements)]
        maxScores = [[0] * numElements for _ in range(numElements)]

        for j in range(numElements):
            for i in range(j, -1, -1):
                if i == j:
                    xorScores[i][j] = nums[i]
                else:
                    xorScores[i][j] = xorScores[i][j - 1] ^ xorScores[i + 1][j]

                if i == j:
                    maxScores[i][j] = xorScores[i][j]
                else:
                    maxVal = xorScores[i][j]
                    if i + 1 <= j:
                        maxVal = max(maxVal, maxScores[i + 1][j])
                    if i <= (j - 1):
                        maxVal = max(maxVal, maxScores[i][j - 1])
                    maxScores[i][j] = maxVal

        results = []
        for query in queries:
            left = query[0]
            right = query[1]
            results.append(maxScores[left][right])

        return results