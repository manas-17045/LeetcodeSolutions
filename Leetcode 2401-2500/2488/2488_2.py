# Leetcde 2488: Count Subarrays With Median K
# https://leetcode.com/problems/count-subarrays-with-median-k/
# Solved on 27th of July, 2025
from collections import Counter


class Solution:
    def countSubarrays(self, nums: list[int], k: int) -> int:
        """
        Counts the number of subarrays where k is the median.

        Args:
            nums: A list of integers.
            k: The integer that must be the median of the subarray.

        Returns:
            int: The total count of subarrays.
        """
        # Find the position of k in the array
        try:
            idx = nums.index(k)
        except ValueError:
            # k is guaranteed to be in nums by problem statement
            return 0

        # Build a counter of "balances" to the left of k (including the empty prefix)
        # balance = (# greater than k) - (# less than k)
        left_counts = Counter()
        balance = 0
        left_counts[0] = 1  # empty prefix

        # Walk from k-1 down to 0
        for i in range(idx - 1, -1, -1):
            if nums[i] > k:
                balance += 1
            else:  # nums[i] < k since distinct
                balance -= 1
            left_counts[balance] += 1

        # Now walk from k to the right, accumulating answer
        ans = 0
        right_balance = 0
        # We include idx itself as the start of right side; its value contributes 0 to balance
        for j in range(idx, len(nums)):
            if j > idx:
                # For elements after k, update the balance similarly
                if nums[j] > k:
                    right_balance += 1
                else:  # nums[j] < k
                    right_balance -= 1

            # A subarray from some left i to this j will have total balance:
            #   left_balance + right_balance
            # We want that total to be 0 or 1:
            #   left_balance = -right_balance  OR left_balance = 1 - right_balance
            ans += left_counts[-right_balance]
            ans += left_counts[1 - right_balance]

        return ans