# Leetcode 3251: Find the Count of Monotonic Pairs II
# https://leetcode.com/problems/find-the-count-of-monotonic-pairs-ii/
# Solved on 3rd of June, 2025

class Solution:
    def countOfPairs(self, nums: list[int]) -> int:
        """
        Counts the number of pairs of arrays (arr1, arr2) such that:
        1. arr1 and arr2 have the same length as nums.
        2. 0 <= arr1[i] <= nums[i] and 0 <= arr2[i] <= nums[i] for all i.
        3. arr1[i] + arr2[i] = nums[i] for all i.
        4. arr1 is non-decreasing.
        5. arr2 is non-increasing.

        This problem can be rephrased as counting pairs of arrays (arr1, arr2)
        where 0 <= arr1[i] <= nums[i], arr1[i] + arr2[i] = nums[i], arr1 is non-decreasing,
        and arr2 is non-increasing. The condition on arr2 being non-increasing
        (arr2[i] >= arr2[i+1]) is equivalent to nums[i] - arr1[i] >= nums[i+1] - arr1[i+1]),
        which simplifies to arr1[i+1] - arr1[i] >= nums[i+1] - nums[i].
        """
        MOD = 10 ** 9 + 7
        n = len(nums)
        if n == 0:
            return 0

        # dp_prev[y] = number of ways to make arr1[i - 1] = y
        dp_prev = [0] * (nums[0] + 1)

        for i in range(1, n):
            prevMax = nums[i - 1]
            currMax = nums[i]
            # d_i = max(0, nums[i] - nums[i - 1])
            d = nums[i] - nums[i - 1]
            if d < 0:
                d = 0

            # Build prefix sums of dp_prev
            prefix = [0] * (prevMax + 1)
            running = 0
            for x in range(prevMax + 1):
                running = (running + dp_prev[x]) % MOD
                prefix[x] = running

            # Now build dp_curr for i
            dp_curr = [0] * (currMax + 1)
            # If y < d, dp_curr[y] stays 0
            for y in range(d, currMax + 1):
                mx = y - d
                if mx > prevMax:
                    mx = prevMax
                dp_curr[y] = prefix[mx]

            dp_prev = dp_curr

        # The answer is sum(dp_prev[y]) for y in [0...nums[n - 1]]
        return sum(dp_prev) % MOD