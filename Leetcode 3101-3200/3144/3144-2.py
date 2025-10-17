# Leetcode 3144: Minimum Substring Partition of Equal Character Frequency
# https://leetcode.com/problems/minimum-substring-partition-of-equal-character-frequency/
# Solved on 17th of October, 2025
class Solution:
    def minimumSubstringsInPartition(self, s: str) -> int:
        """
        Calculates the minimum number of balanced substrings a given string can be partitioned into.
        :param s: The input string.
        :return: The minimum number of balanced substrings.
        """
        n = len(s)
        INF = 10**9
        dp: list[int] = [INF] * (n + 1)
        dp[0] = 0

        for i in range(1, (n + 1)):
            counts = [0] * 26
            # Build substring s[j:i] by expanding j backwards
            for j in range(i - 1, -1, -1):
                counts[ord(s[j]) - 97] += 1

                # Check balanced: all non-zero counts must be equal
                target = None
                balanced = True
                for c in counts:
                    if c > 0:
                        if target is None:
                            target = c
                        elif c != target:
                            balanced = False
                            break

                if balanced:
                    dp[i] = min(dp[i], dp[j] + 1)

        return dp[n]