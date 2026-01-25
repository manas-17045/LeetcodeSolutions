# Leetcode 1984: Minimum Difference Between Highest and Lowest of K Scores
# https://leetcode.com/problems/minimum-difference-between-highest-and-lowest-of-k-scores/
# Solved on 25th of January, 2026
class Solution:
    def minimumDifference(self, nums: list[int], k: int) -> int:
        """
        Finds the minimum possible difference between the highest and lowest of any k scores.

        Args:
            nums (list[int]): A list of student scores.
            k (int): The number of scores to pick.

        Returns:
            int: The minimum possible difference.
        """
        if k == 1:
            return 0

        nums.sort()
        minDifference = float('inf')

        for i in range(len(nums) - k + 1):
            currentDifference = nums[i + k - 1] - nums[i]
            if currentDifference < minDifference:
                minDifference = currentDifference

        return int(minDifference)