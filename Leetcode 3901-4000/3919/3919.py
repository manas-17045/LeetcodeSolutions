# Leetcode 3919: Minimum Cost to Move Between Indices
# https://leetcode.com/problems/minimum-cost-to-move-between-indices/
# Solved on 19th of May, 2026
class Solution:
    def minCost(self, nums: list[int], queries: list[list[int]]) -> list[int]:
        """
        Calculates the minimum cost to move between indices based on proximity rules.

        :param nums: A list of integers representing positions.
        :param queries: A list of [start, end] index pairs.
        :return: A list of minimum costs for each query.
        """
        arrayLen = len(nums)
        prefixCost = [0] * arrayLen
        suffixCost = [0] * arrayLen

        for i in range(arrayLen - 1):
            if i == 0 or nums[i + 1] - nums[i] < nums[i] - nums[i - 1]:
                moveCost = 1
            else:
                moveCost = nums[i + 1] - nums[i]
            prefixCost[i + 1] = prefixCost[i] + moveCost

        for i in range(arrayLen - 1, 0, -1):
            if i == arrayLen - 1 or nums[i] - nums[i - 1] <= nums[i + 1] - nums[i]:
                moveCost = 1
            else:
                moveCost = nums[i] - nums[i - 1]
            suffixCost[i - 1] = suffixCost[i] + moveCost

        answerArray = []
        for currentQuery in queries:
            startIdx = currentQuery[0]
            endIdx = currentQuery[1]
            if startIdx < endIdx:
                answerArray.append(prefixCost[endIdx] - prefixCost[startIdx])
            else:
                answerArray.append(suffixCost[endIdx] - suffixCost[startIdx])

        return answerArray