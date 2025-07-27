# Leetcode 2763: Sum of Imbalance Numbers of All Subarrays
# https://leetcode.com/problems/sum-of-imbalance-numbers-of-all-subarrays/
# Solved on 27th of July, 2025
class Solution:
    def sumImbalanceNumbers(self, nums: list[int]) -> int:
        """
        Calculates the sum of imbalance numbers for all possible subarrays of the given array.
        An imbalance number for a subarray is defined as the number of segments formed by
        consecutive elements when the subarray is sorted, minus one.

        Args:
            nums (list[int]): The input list of integers.
        Returns:
            int: The total sum of imbalance numbers across all subarrays.
        """
        n = len(nums)
        # Since 1 <= nums[i] <= n, we can size presence to n+2 safely
        presence = [False] * (n + 3)
        total = 0

        # For each possible subarray start
        for i in range(n):
            # Reset presence and segment count
            for x in range(1, n + 1):
                presence[x] = False
            segments = 0

            # Grow the subarray to the right
            for j in range(i, n):
                x = nums[j]
                if not presence[x]:
                    left = presence[x - 1]
                    right = presence[x + 1]
                    # New isolated value: creates a new segment
                    if not left and not right:
                        segments += 1
                    # Bridges two existing segments: merges segments
                    elif left and right:
                        segments -= 1
                    # Otherwise it just extends one existing segment (no change)
                    presence[x] = True
                # Each subarray’s imbalance = (#segments) - 1
                total += segments - 1

        return total