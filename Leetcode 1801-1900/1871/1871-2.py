# Leetcode 1871: Jump Game VII
# https://leetcode.com/problems/jump-game-vii/
# Solved on 31st of August, 2025
class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        """
        Determines if the last index of a binary string 's' can be reached from the first index (index 0).
        A jump is possible from index 'i' to index 'j' if s[j] == '0' and minJump <= j - i <= maxJump.

        Args:
            s (str): A binary string where '0' represents a reachable position and '1' represents an obstacle.
            minJump (int): The minimum length of a jump.
            maxJump (int): The maximum length of a jump.

        Returns:
            bool: True if the last index can be reached, False otherwise.
        """
        n = len(s)
        dp = [False] * n
        dp[0] = True

        # Sliding window count of dp[j] for j in [i - maxJump, i - minJump]
        count = 0

        for i in range(1, n):
            # Include dp[i - minJump] into the window if itb exists
            if i - minJump >= 0 and dp[i - minJump]:
                count += 1

            # Exclude dp[i - maxJump - 1] from the window if it exists
            if i - maxJump - 1 >= 0 and dp[i - maxJump - 1]:
                count -= 1

            # i is reachable if there's at least one reachable index in the window
            if s[i] == '0' and count > 0:
                dp[i] = True

        return dp[-1]