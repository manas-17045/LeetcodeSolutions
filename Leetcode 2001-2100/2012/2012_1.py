# Leetcode 2012: Sum of Beauty in the Array
# https://leetcode.com/problems/sum-of-beauty-in-the-array/
# Solved on 28th of June, 2025
class Solution:
    def sumOfBeauties(self, nums: list[int]) -> int:
        """
        Calculates the total beauty of an array based on specific conditions.

        The beauty of an element nums[i] (where 0 < i < n - 1) is defined as:
        - 2 if nums[j] < nums[i] < nums[k] for all 0 <= j < i and i < k < n.
        - 1 if nums[i-1] < nums[i] < nums[i+1] (and the above condition is not met).
        - 0 otherwise.

        The total beauty is the sum of the beauty of all such elements.

        Args:
            nums: A list of integers.

        Returns:
            The total beauty of the array.
        """
        n = len(nums)
        totalBeauty = 0

        rightMin = [0] * n
        rightMin[n - 1] = nums[n - 1]
        for i in range(n - 2, -1, -1):
            rightMin[i] = min(rightMin[i + 1], nums[i])

        leftMax = nums[0]
        for i in range(1, (n - 1)):
            if leftMax < nums[i] and nums[i] < rightMin[i + 1]:
                totalBeauty += 2
            elif nums[i - 1] < nums[i] and nums[i] < nums[i + 1]:
                totalBeauty += 1

            leftMax = max(leftMax, nums[i])

        return totalBeauty