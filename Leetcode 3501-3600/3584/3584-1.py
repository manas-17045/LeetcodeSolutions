# Leetcode 3584: Maximum Product of First and Last Elements of a Subsequence
# https://leetcode.com/problems/maximum-product-of-first-and-last-elements-of-a-subsequence/
# Solved on 4th of October, 2025
class Solution:
    def maximumProduct(self, nums: list[int], m: int) -> int:
        """
        Calculates the maximum product of the first and last elements of a subsequence of length m.

        Args:
            nums (list[int]): The input list of integers.
            m (int): The desired length of the subsequence.
        Returns:
            int: The maximum product found.
        """
        n = len(nums)

        if m == 1:
            maxProd = float('-inf')
            for num in nums:
                maxProd = max(maxProd, num * num)
            return int(maxProd)

        prefixMax = [0] * n
        prefixMin = [0] * n

        prefixMax[0] = nums[0]
        prefixMin[0] = nums[0]

        for i in range(1, n):
            prefixMax[i] = max(prefixMax[i - 1], nums[i])
            prefixMin[i] = min(prefixMin[i - 1], nums[i])

        maxProd = float('-inf')

        for j in range((m - 1), n):
            k = j - m + 1

            maxPrefix = prefixMax[k]
            minPrefix = prefixMin[k]

            lastVal = nums[j]

            prod1 = maxPrefix * lastVal
            prod2 = minPrefix * lastVal

            maxProd = max(maxProd, prod1, prod2)

        return int(maxProd)