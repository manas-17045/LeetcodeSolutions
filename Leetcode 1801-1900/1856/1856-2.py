# Leetcode 1856: Maximum Subarray Min-Product
# https://leetcode.com/problems/maximum-subarray-min-product/
# Solved on 29th of August, 2025
class Solution:
    def maxSumMinProduct(self, nums: list[int]) -> int:
        """
        Calculates the maximum score of a subarray, where the score is defined as the minimum value in the subarray
        multiplied by the sum of all elements in the subarray.

        :param nums: A list of integers.
        :return: The maximum score modulo 10^9 + 7.
        """
        MOD = 10 ** 9 + 7
        n = len(nums)
        # prefix sums: prefix[i] = sum of nums[:i]
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]

        # previous index with value < nums[i]
        prev_less = [-1] * n
        stack = []
        for i in range(n):
            # pop indices whose value >= current so top becomes previous < current
            while stack and nums[stack[-1]] >= nums[i]:
                stack.pop()
            prev_less[i] = stack[-1] if stack else -1
            stack.append(i)

        # next index with value < nums[i]
        next_less = [n] * n
        stack.clear()
        for i in range(n - 1, -1, -1):
            # pop indices whose value > current so top becomes next < current
            while stack and nums[stack[-1]] > nums[i]:
                stack.pop()
            next_less[i] = stack[-1] if stack else n
            stack.append(i)

        max_prod = 0
        for i in range(n):
            left = prev_less[i] + 1
            right = next_less[i] - 1
            total = prefix[right + 1] - prefix[left]
            prod = nums[i] * total
            if prod > max_prod:
                max_prod = prod

        return max_prod % MOD