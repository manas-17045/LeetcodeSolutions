# Leetcode 2602: Minimum Operations to Make All Array Elements Equal
# https://leetcode.com/problems/minimum-operations-to-make-all-array-elements-equal/
# Solved on 28th of November, 2025
import bisect
from itertools import accumulate


class Solution:
    def minOperations(self, nums: list[int], queries: list[int]) -> list[int]:
        """
        Calculates the minimum operations required to make all elements in `nums` equal to each query.
        :param nums: A list of integers.
        :param queries: A list of integers representing the target values.
        :return: A list of integers, where each element is the minimum operations for the corresponding query.
        """
        nums.sort()
        n = len(nums)
        prefixSum = [0] + list(accumulate(nums))
        answer = []

        for query in queries:
            index = bisect.bisect_left(nums, query)

            leftOperations = (index * query) - prefixSum[index]
            rightOperations = (prefixSum[n] - prefixSum[index]) - ((n - index) * query)

            answer.append(leftOperations + rightOperations)

        return answer