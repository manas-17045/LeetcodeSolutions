# Leetcode 2035: Partition Array Into Two Arrays to Minimize Sum Difference
# https://leetcode.com/problems/partition-array-into-two-arrays-to-minimize-sum-difference/
# Solved on 29th of June, 2025
import bisect


class Solution:
    def minimumDifference(self, nums: list[int]) -> int:
        """
        Partitions the input array `nums` into two arrays of equal length `n`
        such that the absolute difference between their sums is minimized.

        This problem is solved using a meet-in-the-middle approach.
        The array `nums` is split into two halves. For each half, all possible
        subset sums are generated, grouped by the number of elements in the subset.
        Then, for each possible number of elements `k` taken from the left half,
        `n-k` elements must be taken from the right half. The goal is to find
        a combination of `leftSum` and `rightSum` such that `leftSum + rightSum`
        is as close as possible to `totalSum / 2`.

        Args:
            nums: A list of integers with an even length.
        """
        n = len(nums) // 2
        totalSum = sum(nums)

        def generateSubsetSums(arr):
            sumsByCount = [set() for _ in range(n + 1)]
            sumsByCount[0].add(0)

            for num in arr:
                for k in range(n, 0, -1):
                    for s in sumsByCount[k - 1]:
                        sumsByCount[k].add(s + num)

            return sumsByCount

        leftHalf = nums[:n]
        rightHalf = nums[n:]

        leftSumsByCount = generateSubsetSums(leftHalf)
        rightSumsByCount = generateSubsetSums(rightHalf)

        for k in range(n + 1):
            rightSumsByCount[k] = sorted(list(rightSumsByCount[k]))

        minDiff = float('inf')

        for leftK in range(n + 1):
            rightK = n - leftK
            rightSumList = rightSumsByCount[rightK]

            for leftSum in leftSumsByCount[leftK]:
                target = (totalSum / 2) - leftSum

                idx = bisect.bisect_left(rightSumList, target)

                if idx < len(rightSumList):
                    rightSum = rightSumList[idx]
                    currentSum = leftSum + rightSum
                    minDiff = min(minDiff, abs(totalSum - 2 * currentSum))

                if idx > 0:
                    rightSum = rightSumList[idx - 1]
                    currentSum = leftSum + rightSum
                    minDiff = min(minDiff, abs(totalSum - 2 * currentSum))

        return int(minDiff)