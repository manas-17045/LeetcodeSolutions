# Leetcode 1755: Closest Subsequence Sum
# https://leetcode.com/problems/closest-subsequence-sum/
# Solved on 29th of June, 2025
import bisect


class Solution:
    def minAbsDifference(self, nums: list[int], goal: int) -> int:
        """
        Finds the minimum absolute difference between a subsequence sum and a given goal.

        This problem is solved using a meet-in-the-middle approach. The input array `nums`
        is split into two halves. All possible subsequence sums are generated for each half.
        Then, for each sum from the first half, we try to find a sum from the second half
        that makes the total sum as close as possible to the `goal`.

        Args:
            nums: A list of integers.
            goal: The target integer.
        Returns:
            The minimum absolute difference between any subset sum of `nums` and `goal`.
        """
        def generateSums(arr):
            sums = {0}
            for num in arr:
                newSums = set()
                for s in sums:
                    newSums.add(s + num)
                sums.update(newSums)
            return sums

        n = len(nums)
        firstHalf = nums[:n//2]
        secondHalf = nums[n//2:]

        sums1 = generateSums(firstHalf)
        sums2 = sorted(list(generateSums(secondHalf)))

        minDiff = float('inf')

        for s1 in sums1:
            target = goal - s1

            # Find the insertion point for target in sums2
            idx = bisect.bisect_left(sums2, target)

            # Check the element at the insertion point
            if idx < len(sums2):
                s2 = sums2[idx]
                minDiff = min(minDiff, abs(s1 + s2 - goal))

            # Check the element before the insertion point
            if idx > 0:
                s2 = sums2[idx - 1]
                minDiff = min(minDiff, abs(s1 + s2 - goal))

        return minDiff