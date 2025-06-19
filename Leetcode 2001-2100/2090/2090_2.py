# Leetcode 2090: K Radius Subarray Averages
# https://leetcode.com/problems/k-radius-subarray-problems/
# Solved on 19th of June, 2025

class Solution:
    def getAverages(self, nums: list[int], k: int) -> list[int]:
        """
        Calculates the k-radius subarray averages for each element in the input list.

        Args:
            nums: A list of integers.
            k: The radius for the subarray.

        Returns:
            A list of integers where each element is the average of the k-radius
            subarray centered at the corresponding index, or -1 if the subarray
            does not fit within the bounds of the list.
        """
        n = len(nums)
        window = 2 * k + 1
        # Initialize all to -1
        ans = [-1] * n

        # If the full window never fits, we're done
        if window > n:
            return ans

        # Build prefix sums
        ps = [0] * (n + 1)
        for i in range(n):
            ps[i + 1] = ps[i] + nums[i]

        # For each i where [(i - k)...(i + k)] is n-bounds, compute average
        for i in range(k, (n - k)):
            total = ps[i + k + 1] - ps[i - k]
            ans[i] = total // window

        return ans