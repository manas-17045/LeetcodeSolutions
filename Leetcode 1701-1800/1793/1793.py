# Leetcode 1793: Maximum Score of a Good Subarray
# https://leetcode.com/problems/maximum-score-of-a-good-subarray/
# Solved on 8th of November, 2025
class Solution:
    def maximumScore(self, nums: list[int], k: int) -> int:
        """
        Calculates the maximum score of a "good" subarray.

        Args:
            nums (list[int]): The input array of integers.
            k (int): The index that must be included in the subarray.
        Returns:
            int: The maximum score of a good subarray.
        """
        n = len(nums)
        left = k
        right = k
        currentMin = nums[k]
        maxScore = nums[k]

        while left > 0 or right < n - 1:
            leftVal = nums[left - 1] if left > 0 else 0
            rightVal = nums[right + 1] if right < n - 1 else 0

            if leftVal > rightVal:
                left -= 1
                currentMin = min(currentMin, leftVal)
            else:
                right += 1
                currentMin = min(currentMin, rightVal)

            maxScore = max(maxScore, currentMin * (right - left + 1))

        return maxScore