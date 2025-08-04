# Leetcode 2968: Apply Operations to Maximize Frequency Score
# https://leetcode.com/problems/apply-operations-to-maximize-frequency-score/
# Solved on 4th of August, 2025
class Solution:
    def maxFrequencyScore(self, nums: list[int], k: int) -> int:
        """
        Calculates the maximum frequency score achievable from a list of numbers.

        Args:
            nums (list[int]): A list of integers.
            k (int): The maximum allowed cost.
        """
        n = len(nums)
        nums.sort()
        ps = [0] * (n + 1)
        for i in range(n):
            ps[i + 1] = ps[i] + nums[i]

        ans = 1
        l = 0
        for r in range(n):
            while l <= r:
                m = (l + r) // 2
                median = nums[m]
                left_count = m - l + 1
                sum_left = ps[m + 1] - ps[l]
                cost_left = median * left_count - sum_left

                right_count = r - m
                sum_right = ps[r + 1] - ps[m + 1]
                cost_right = sum_right - median * right_count
                total_cost = cost_left + cost_right

                if total_cost <= k:
                    break
                l += 1

            # Window [l...r] is feasible
            ans = max(ans, r - l + 1)

        return ans