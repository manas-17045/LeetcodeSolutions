# Leetcode 1982: Find Array Given Subset Sums
# https://leetcode.com/problems/find-array-given-subset-sums/
# Solved on 5th of July, 2025
import collections


class Solution:
    def recoverArray(self, n: int, sums: list[int]) -> list[int]:
        """
        Recovers the original array of `n` integers given the sums of all its 2^n subsets.

        The core idea is to iteratively determine one element of the original array at a time.
        In each step, we identify a candidate element `d` (or `-d`) by observing the difference
        between the largest two subset sums. This difference `d` represents the absolute value
        of an element that was added to one half of the subsets to form the other half.

        We partition the current set of `sums` into two groups: those that include `d` and
        those that do not. One of these groups will represent the subset sums of the array
        with one element removed. We determine which group by checking if it contains 0
        (as the empty set sum must always be present).

        Args:
            n (int): The number of elements in the original array.
            sums (list[int]): A list of 2^n integers representing all possible subset sums.

        Returns:
            list[int]: The recovered original array of `n` integers.
        """
        ans = []
        sums.sort()

        for currentN in range(n, 0, -1):
            # Find a candidate element. This difference `d` will be positive.
            d = sums[-1] - sums[-2]

            # Use a frequency map for efficient partitioning.
            counts = collections.Counter(sums)
            nextSums = []

            # Partition `sums` into two groups. We only need to construct one.
            # Iterating from largest to smallest is crucial when d > 0.
            for s in reversed(sums):
                if counts[s] > 0:
                    partner = s - d
                    # The element s belongs to one partition, its partner to the other.
                    # We add the partner to our candidate list for the next subproblem.
                    nextSums.append(partner)
                    counts[s] -= 1
                    counts[partner] -= 1

            # Decode if the element was `d` or `-d`.
            # The correct subproblem must contain 0 as a subset sum.
            if 0 in collections.Counter(nextSums):
                ans.append(d)
                sums = sorted(nextSums)
            else:
                ans.append(-d)
                sums = sorted([(x + d) for x in nextSums])

        return ans