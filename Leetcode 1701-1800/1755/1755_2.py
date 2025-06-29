# Leetcode 1755: Closest Subsequence Sum
# https://leetcode.com/problems/closest-subsequence-sum/
# Solved on 29th of June, 2025
import bisect


class Solution:
    def minAbsDifference(self, nums: list[int], goal: int) -> int:
        """
        Finds the minimum absolute difference between a subset sum of `nums` and `goal`.

        This problem is solved using the "Meet-in-the-Middle" technique.
        The input array `nums` is split into two halves. All possible subset sums
        are generated for each half. Then, for each sum from the first half,
        a binary search is performed on the sorted sums of the second half
        to find a sum that, when combined, gets as close as possible to `goal`.

        Args:
            nums: A list of integers.
            goal: The target integer.
        """
        n = len(nums)
        mid = n // 2
        left, right = nums[:mid], nums[mid:]

        # Generate all subset sums of arr into out
        def gen_sums(arr, idx, curr, out):
            if idx == len(arr):
                out.append(curr)
            else:
                gen_sums(arr, idx + 1, curr, out)
                gen_sums(arr, idx + 1, curr + arr[idx], out)

        a_sums, b_sums = [], []
        gen_sums(left, 0, 0, a_sums)
        gen_sums(right, 0, 0, b_sums)

        # Sort one list for binary search
        b_sums.sort()

        # Best so far: taking nothing from both halves
        best = abs(goal)

        # For every sum in a_sums, find closest in b_sums
        for s in a_sums:
            # Remaining, we want from b_sums
            target = goal - s
            i = bisect.bisect_left(b_sums, target)

            # Check the candidate at i
            if i < len(b_sums):
                curr_diff = abs(s + b_sums[i] - goal)
                if curr_diff < best:
                    best = curr_diff

            # And the one just before
            if i > 0:
                curr_diff = abs(s + b_sums[i - 1] - goal)
                if curr_diff < best:
                    best = curr_diff

            # Early exit if perfect match found
            if best == 0:
                return 0

        return best