# Leetcode 1871: Jump Game VII
# https://leetcode.com/problems/jump-game-vii/
# Solved on 31st of August, 2025
class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        """
        Determines if it's possible to reach the last index of a binary string `s`
        starting from index 0, by making jumps within a specified range.

        :param s: A binary string where '0' represents a reachable position and '1' an unreachable one.
        :param minJump: The minimum length of a jump.
        :param maxJump: The maximum length of a jump.
        :return: True if the last index can be reached, False otherwise.
        """
        n = len(s)
        dp = [False] * n
        dp[0] = s[0] == '0'
        reachableCount = 0

        if not dp[0]:
            return False

        for i in range(1, n):
            if i >= minJump:
                if dp[i - minJump]:
                    reachableCount += 1

            if i > maxJump:
                if dp[i - maxJump - 1]:
                    reachableCount -= 1

            if s[i] == '0' and reachableCount > 0:
                dp[i] = True

        return dp[n - 1]