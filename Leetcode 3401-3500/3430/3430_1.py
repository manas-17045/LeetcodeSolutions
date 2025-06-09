# Leetcode 3430: Maximum and Minimum Sums of at Most Size K Subarrays
# https://leetcode.com/problems/maximum-and-minimum-sums-of-at-most-size-k-subarrays/
# Solved on 9th of June, 2025
from typing import Callable


class Solution:
    def minMaxSubarraySum(self, nums: list[int], k: int) -> int:
        """
        Calculates the sum of maximums and the sum of minimums of all subarrays
        of `nums` with a size of at most `k`.

        The approach uses the concept of "contribution of each element". For each element
        `nums[i]`, we determine how many subarrays of size at most `k` it is the maximum
        in, and how many it is the minimum in. The total sum is the sum of (element * count)
        for all elements and for both maximum and minimum roles.

        Args:
            nums: The input list of integers.
            k: The maximum size of the subarrays to consider.

        Returns:
            The total sum of maximums and minimums of all valid subarrays.
        """
        n = len(nums)

        def getPrev(comp: Callable[[int, int], bool]) -> list[int]:
            prev = [-1] * n
            stack = []
            for i in range(n):
                while stack and not comp(nums[stack[-1]], nums[i]):
                    stack.pop()
                if stack:
                    prev[i] = stack[-1]
                stack.append(i)
            return prev

        def getNext(comp: Callable[[int, int], bool]) -> list[int]:
            nextVal = [n] * n
            stack = []
            for i in range(n - 1, -1, -1):
                while stack and not comp(nums[stack[-1]], nums[i]):
                    stack.pop()
                if stack:
                    nextVal[i] = stack[-1]
                stack.append(i)
            return nextVal

        def countValid(nl: int, nr: int, kLimit: int) -> int:
            p = kLimit - 1

            def N(t: int) -> int:
                if t < 0:
                    return 0
                return (t + 1) * (t + 2) // 2

            val = N(p) - N(p - nl - 1) - N(p - nr - 1) + N(p - nl - nr - 2)
            return val

        def calculateContribution(leftArr: list[int], rightArr: list[int]) -> int:
            totalContribution = 0
            for i in range(n):
                lBound = leftArr[i]
                rBound = rightArr[i]

                nl = i - lBound - 1
                nr = rBound - i - 1

                count = countValid(nl, nr, k)
                totalContribution += nums[i] * count

            return totalContribution

        # For sum of maximums, we use left >= and right > to partition subarrays.
        leftG = getPrev(lambda x, y: x >= y)
        rightG = getNext(lambda x, y: x > y)

        # For sum of minimums, we use left < and right <= to partition
        leftL = getPrev(lambda x, y: x < y)
        rightL = getNext(lambda x, y: x <= y)

        totalSum = 0
        totalSum += calculateContribution(leftG, rightG)
        totalSum += calculateContribution(leftL, rightL)

        return totalSum