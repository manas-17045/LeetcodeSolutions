# Leetcode 2770: Maximum Number of Jumps to Reach the Last Index
# https://leetcode.com/problems/maximum-number-of-jumps-to-reach-the-last-index/
# Solved on 31st of August, 2025
class Solution:
    def maximumJumps(self, nums: list[int], target: int) -> int:
        """
        Calculates the maximum number of jumps possible to reach the end of the array.
        :param nums: A list of integers representing the array.
        :param target: An integer representing the maximum allowed difference between nums[j] and nums[i].
        :return: The maximum number of jumps, or -1 if the end is unreachable.
        """
        n = len(nums)
        # Sentinel for unreachable
        NEG = -10**9
        dp = [NEG] * n
        dp[0] = 0

        for i in range(n):
            if dp[i] == NEG:
                # Can't reach i, SKIP
                continue

            # Try jump from i to any j > i
            ai = nums[i]
            for j in range(i + 1, n):
                if -target <= nums[j] - ai <= target:
                    # If reachable, update max jumps to j
                    dp[j] = max(dp[j], dp[i] + 1)

        return dp[-1] if dp[-1] != NEG else -1