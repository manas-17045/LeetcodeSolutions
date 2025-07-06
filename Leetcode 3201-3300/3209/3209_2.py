# Leetcode 3209: Number of Subarrays With AND Value of K
# https://leetcode.com/problems/number-of-subarrays-with-and-value-of-k/
# Solved on 6th of July, 2025
from collections import Counter


class Solution:
    def countSubarrays(self, nums: list[int], k: int) -> int:
        """
        Counts the number of subarrays whose bitwise AND sum equals k.

        This method iterates through the array, maintaining a count of all possible
        AND sums ending at the current position. It leverages the property that
        ANDing with a new number can only decrease or keep the value the same.

        Args:
            nums: The input list of integers.
            k: The target bitwise AND sum.
        """
        count = 0
        # prev_and[c] = number of subarrays ending at the previous index with bitwise-AND = c
        prev_and = Counter()

        for x in nums:
            # Start a new subarray at x alone
            curr_and = Counter({x: 1})

            # Extend all previous subarrays by including x
            for val, freq in prev_and.items():
                new_val = val & x
                curr_and[new_val] += freq

            # Add how many of these ending here have AND == k
            count += curr_and.get(k, 0)

            # Roll forward
            prev_and = curr_and

        return count