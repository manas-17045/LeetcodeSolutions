# Leetcode 2767: Partition String Into Minimum Beautiful Substrings
# https://leetcode.com/problems/partition-string-into-minimum-beautiful-substrings/
# Solved on 17th of October, 2025
class Solution:
    def minimumBeautifulSubstrings(self, s: str) -> int:
        """
        Calculates the minimum number of beautiful substrings a binary string can be split into.
        A beautiful substring is a binary representation of a power of 5, with no leading zeros.
        :param s: The input binary string.
        :return: The minimum number of beautiful substrings, or -1 if no such partition exists.
        """
        # Generate all powers of 5 in binary representation up to length 15
        powers_of_5 = set()
        power = 1
        while len(bin(power)[2:]) <= 15:
            powers_of_5.add(bin(power)[2:])
            power *= 5

        n = len(s)

        # Initialize dynamic programming with infinity
        dp = [float('inf')] * (n + 1)
        dp[0] = 0

        for i in range(1, n + 1):
            # Try all possible substrings ending at position i
            for j in range(i):
                substring = s[j:i]

                # check if this substring is beautiful
                if substring[0] != '0' and substring in powers_of_5:
                    # Update dp[i] if we can form a better partition
                    dp[i] = min(dp[i], dp[j] + 1)

        return dp[n] if dp[n] != float('inf') else -1