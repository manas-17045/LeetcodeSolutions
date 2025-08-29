# Leetcode 1248: Count Number of Nice Subarrays
# https://leetcode.com/problems/count-number-of-nice-subarrays/
# Solved on 29th of August, 2025
class Solution:
    def numberOfSubarrays(self, nums: list[int], k: int) -> int:
        """
        Calculates the number of "nice" subarrays. A "nice" subarray is defined as a continuous subarray
        with exactly `k` odd numbers.
        :param nums: A list of integers.
        :param k: The required number of odd integers in a "nice" subarray.
        :return: The total count of "nice" subarrays.
        """
        n = len(nums)
        # Collect indices of odd numbers
        odd_idx = [-1]
        for i, val in enumerate(nums):
            if val % 2 == 1:
                odd_idx.append(i)
        odd_idx.append(n)

        # If there are fewer than k odds, no nice subarray exists.
        total_odds = len(odd_idx) - 2
        if total_odds < k:
            return 0

        ans = 0
        # For each group of k consecutive odd indices,
        # multiply to get number of subarrays using exactly these k odds.
        for start in range(1, total_odds - k + 2):
            left_choices = odd_idx[start] - odd_idx[start - 1]
            right_choices = odd_idx[start + k] - odd_idx[start + k - 1]
            ans += left_choices * right_choices

        return ans