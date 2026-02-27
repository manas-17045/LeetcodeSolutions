# Leetcode 3213: Construct String with Minimum Cost
# https://leetcode.com/problems/construct-string-with-minimum-cost/
# Solved on 27th of February, 2026
class Solution:
    def minimumCost(self, target: str, words: list[str], costs: list[int]) -> int:
        """
        Calculates the minimum cost to construct the target string using a given list of words and their costs.

        :param target: The string to be constructed.
        :param words: A list of strings available to construct the target.
        :param costs: A list of integers representing the cost of using each word in 'words'.
        :return: The minimum total cost to construct 'target', or -1 if it's impossible.
        """
        targetLen = len(target)
        infinity = 10**18
        dp = [infinity] * (targetLen + 1)
        dp[0] = 0

        wordCosts = {}
        for i in range(len(words)):
            word = words[i]
            cost = costs[i]
            if word not in wordCosts or cost < wordCosts[word]:
                wordCosts[word] = cost

        uniqueLengths = sorted(list(set(len(w) for w in wordCosts.keys())))

        for i in range(targetLen):
            if dp[i] == infinity:
                continue

            for length in uniqueLengths:
                if (i + length) > targetLen:
                    break

                subStr = target[i : i + length]
                if subStr in wordCosts:
                    newCost = dp[i] + wordCosts[subStr]
                    if newCost < dp[i + length]:
                        dp[i + length] = newCost

        return dp[targetLen] if dp[targetLen] != infinity else -1