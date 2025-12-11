# Leetcode 2911: Minimum Changes to Make K Semi-palindromes
# https://leetcode.com/problems/minimum-changes-to-make-k-semi-palindromes/
# Solved on 11th of December, 2025
class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        """
        Calculates the minimum changes required to make k semi-palindromes from string s.

        Args:
            s (str): The input string.
            k (int): The number of semi-palindromes to form.
        Returns:
            int: The minimum number of changes required.
        """

        n = len(s)
        divisors = [[] for _ in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(i * 2, n + 1, i):
                divisors[j].append(i)

        costs = [[0] * n for _ in range(n)]
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                minCost = float('inf')
                for d in divisors[length]:
                    currentCost = 0
                    for offset in range(d):
                        left = i + offset
                        right = j - (d - 1 - offset)
                        while left < right:
                            if s[left] != s[right]:
                                currentCost += 1
                            left += d
                            right -= d
                    if currentCost < minCost:
                        minCost = currentCost
                costs[i][j] = minCost

        dp = [float('inf')] * n
        for i in range(1, n):
            dp[i] = costs[0][i]

        for parts in range(2, k + 1):
            newDp = [float('inf')] * n
            for i in range(parts * 2 - 1, n):
                for prev in range((parts - 1) * 2 - 1, i - 1):
                    cost = dp[prev] + costs[prev + 1][i]
                    if cost < newDp[i]:
                        newDp[i] = cost
            dp = newDp

        return int(dp[n - 1])