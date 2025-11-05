# Leetcode 2919: Minimum Increment Operations to Make Array Beautiful
# https://leetcode.com/problems/minimum-increment-operations-to-make-array-beautiful/
# Solved on 5th of November, 2025
class Solution:
    def minIncrementOperations(self, nums: list[int], k: int) -> int:
        """
        Calculates the minimum increment operations to make the array beautiful.
        An array is beautiful if for every `i` from `0` to `n - 3`, at least one of `nums[i]`, `nums[i+1]`, or `nums[i+2]` is greater than or equal to `k`.

        Args:
            nums: A list of integers.
            k: An integer threshold.
        Returns:
            The minimum number of increment operations required.
        """
        n = len(nums)

        dpNext1 = 0
        dpNext2 = 0
        dpNext3 = 0

        for i in range(n - 1, -1, -1):

            currentDp = 0

            if i > n - 3:
                currentDp = 0
            else:
                cost1 = max(0, k - nums[i])
                option1 = cost1 + dpNext1

                cost2 = max(0, k - nums[i + 1])
                option2 = cost2 + dpNext2

                cost3 = max(0, k - nums[i + 2])
                option3 = cost3 + dpNext3

                currentDp = min(option1, option2, option3)

            dpNext3 = dpNext2
            dpNext2 = dpNext1
            dpNext1 = currentDp

        return dpNext1