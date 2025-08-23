# Leetcode 2333: Minimum Sum of Squared Difference
# https://leetcode.com/problems/minimum-sum-of-squared-difference/
# Solved on 23rd of August, 2025
class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        """
        Calculates the minimum sum of squared differences between two arrays after applying at most k1 + k2 operations.

        Args:
            nums1 (list[int]): The first input list of integers.
            nums2 (list[int]): The second input list of integers.
            k1 (int): The maximum number of operations allowed for nums1.
            k2 (int): The maximum number of operations allowed for nums2.

        Returns:
            int: The minimum sum of squared differences.
        """
        n = len(nums1)
        abs_diff = [abs(nums1[i] - nums2[i]) for i in range(n)]

        if n == 0:
            return 0

        d = sorted(abs_diff, reverse=True)
        d.append(0)

        max_k = k1 + k2
        cum_cost = 0
        count = 0

        for i in range(n):
            count += 1
            cur_diff = d[i] - d[i + 1]

            if cur_diff > 0:
                segment_cost = count * cur_diff
                if cum_cost + segment_cost <= max_k:
                    cum_cost += segment_cost
                else:
                    remaining = max_k - cum_cost
                    q = remaining // count
                    extra = remaining % count
                    level1 = d[i] - q
                    level2 = d[i] - q - 1
                    num1 = count - extra
                    num2 = extra
                    sum_sq = num1 * (level1 ** 2) + num2 * (level2 ** 2)
                    for j in range(i + 1, n):
                        sum_sq += d[j] ** 2

                    return sum_sq

        return 0