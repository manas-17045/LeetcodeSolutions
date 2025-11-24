# Leetcode 3441: Minimum Cost Good Caption
# https://leetcode.com/problems/minimum-cost-good-caption/
# Solved on 24th of November, 2025
class Solution:
    def minCostGoodCaption(self, caption: str) -> str:
        """
        Calculates the minimum cost to transform the given caption into a "good caption"
        and returns the resulting good caption.

        :param caption: The input string caption.
        :return: The good caption with the minimum transformation cost, or an empty string if no good caption can be formed.
        """
        n = len(caption)
        if n < 3:
            return ""

        prefixCosts = [[0] * (n + 1) for _ in range(26)]
        for charCode in range(26):
            targetChar = chr(charCode + 97)
            row = prefixCosts[charCode]
            for i, char in enumerate(caption):
                row[i + 1] = row[i] + abs(ord(char) - ord(targetChar))

        dp = [float('inf')] * (n + 1)
        dp[n] = 0

        bestChoice = [None] * (n + 1)

        for i in range(n - 1, -1, -1):
            minCost = float('inf')
            bestChar = -1
            bestLen = -1

            for charCode in range(26):
                minCostForChar = float('inf')
                validLs = []

                # Check possible lengths for the current block
                for length in (3, 4, 5):
                    if i + length <= n:
                        if dp[i + length] == float('inf'):
                            continue

                        costBlock = prefixCosts[charCode][i + length] - prefixCosts[charCode][i]
                        totalCost = costBlock + dp[i + length]

                        if totalCost < minCostForChar:
                            minCostForChar = totalCost
                            validLs = [length]
                        elif totalCost == minCostForChar:
                            validLs.append(length)

                if minCostForChar == float('inf'):
                    continue

                # Update global minimum for this position i
                if minCostForChar < minCost:
                    minCost = minCostForChar
                    bestChar = charCode

                    # Tie-breaking logic for lengths with same cost
                    bestLen = validLs[0]
                    for j in range(1, len(validLs)):
                        candidate_L = validLs[j]

                        p1_char_idx = bestChoice[i + bestLen][0]

                        if p1_char_idx != charCode:
                            if p1_char_idx < charCode:
                                pass
                            else:
                                bestLen = candidate_L
                        else:
                            if i + candidate_L == n:
                                pass
                            else:
                                p2_char_idx = bestChoice[i + candidate_L][0]
                                if p2_char_idx < charCode:
                                    bestLen = candidate_L
                                else:
                                    pass

            dp[i] = minCost
            bestChoice[i] = (bestChar, bestLen)

        if dp[0] == float('inf'):
            return ""

        # Reconstruct the string
        res = []
        curr = 0
        while curr < n:
            charIdx, length = bestChoice[curr]
            res.append(chr(charIdx + 97) * length)
            curr += length

        return "".join(res)