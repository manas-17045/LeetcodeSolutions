# Leetcode 2585: Number of Ways to Earn Points
# https://leetcode.com/problems/number-of-ways-to-earn-points/
# Solved on 13th of August, 2025
class Solution:
    def waysToReachTarget(self, target: int, types: list[list[int]]) -> int:
        """
        Calculates the number of ways to reach a target score using different types of problems.

        Args:
            target (int): The target score to reach.
            types (list[list[int]]): A list of problem types, where each type is [count, marks].
                                     'count' is the number of problems of this type available,
                                     and 'marks' is the score obtained for solving one problem of this type.

        Returns:
            int: The number of ways to reach the target score, modulo 10^9 + 7.
        """
        MOD = 10**9 + 7
        # dp[s] = number of ways to get score s using processed types so far
        dp = [0] * (target + 1)
        dp[0] = 1

        for count, marks in types:
            # New will become do after considering this type
            new = [0] * (target + 1)

            # Process each residue class modulo marks
            # Indices of the form r + q * marks form an arithmetic sequence
            for r in range(marks):
                window_sum = 0
                q = 0
                for idx in range(r, target + 1, marks):
                    # Add current dp value (corresponds to taking t = 0 for this position)
                    window_sum = (window_sum + dp[idx]) % MOD
                    # If window is larger than count + 1, remove the farthest element
                    if q - (count + 1) >= 0:
                        rem_idx = r + (q - (count + 1)) * marks
                        window_sum = (window_sum - dp[rem_idx]) % MOD
                    new[idx] = window_sum
                    q += 1

            dp = new

        return dp[target] % MOD