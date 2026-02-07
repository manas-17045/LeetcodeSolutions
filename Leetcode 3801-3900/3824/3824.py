# Leetcode 3824: Minimum K to Reduce Array Within Limit
# https://leetcode.com/problems/minimum-k-to-reduce-array-within-limit/
# Solved on 7th of February, 2026
class Solution:
    def minimumK(self, nums: list[int]) -> int:
        """
        Finds the minimum value of k such that the total operations to reduce all elements
        in nums (where each operation reduces an element by at most k) does not exceed k^2.

        :param nums: List of integers to be reduced.
        :return: The smallest integer k that satisfies the condition.
        """
        low = 1
        high = max(max(nums), int(len(nums) ** 0.5) + 1)
        ans = high

        while low <= high:
            mid = (low + high) // 2
            currentOps = 0
            limit = mid * mid
            canAchieve = True

            for num in nums:
                currentOps += (num + mid - 1) // mid
                if currentOps > limit:
                    canAchieve = False
                    break

            if canAchieve:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans