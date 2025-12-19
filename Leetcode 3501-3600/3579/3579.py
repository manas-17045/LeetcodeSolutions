# Leetcode 3579: Minimum Steps to Convert String with Operations
# https://leetcode.com/problems/minimum-steps-to-convert-string-with-operations/
# Solved on 19th of December, 2025
class Solution:
    def minOperations(self, word1: str, word2: str) -> int:
        """
        Calculates the minimum number of operations to convert word1 to word2.

        Args:
            word1 (str): The source string.
            word2 (str): The target string.
        Returns:
            int: The minimum number of operations.
        """
        n = len(word1)
        dp = [float('inf')] * (n + 1)
        dp[0] = 0

        def getCost(s1, s2):
            diff = 0
            counts = {}
            for c1, c2 in zip(s1, s2):
                if c1 != c2:
                    diff += 1
                    pair = (c1, c2)
                    counts[pair] = counts.get(pair, 0) + 1

            swaps = 0
            visited = set()
            for pair, count in counts.items():
                if pair in visited:
                    continue
                revPair = (pair[1], pair[0])
                if revPair in counts:
                    swaps += min(count, counts[revPair])
                    visited.add(revPair)
                visited.add(pair)

            return diff - swaps

        for i in range(1, n + 1):
            for j in range(i):
                sub1 = word1[j:i]
                sub2 = word2[j:i]

                costNoRev = getCost(sub1, sub2)
                costRev = 1 + getCost(sub1[::-1], sub2)

                currentCost = min(costNoRev, costRev)
                dp[i] = min(dp[i], dp[j] + currentCost)

        return int(dp[n])