# Leetcode 1434: Number of Ways to Wear Different Hats to Each Other
# https://leetcode.com/problems/number-of-ways-to-wear-different-hats-to-each-other/
# Solved on 10th of August, 2025
class Solution:
    def numberWays(self, hats: list[list[int]]) -> int:
        """
        Calculates the number of ways to assign hats to people such that each person wears a different hat.

        Args:
            hats: A list of lists, where hats[i] is a list of preferred hats for the i-th person.
        Returns:
            The number of ways to assign hats, modulo 10^9 + 7.
        """
        numPeople = len(hats)
        mod = 10**9 + 7

        hatToPeople = [[] for _ in range(41)]
        for personId, preferredHats in enumerate(hats):
            for hatId in preferredHats:
                hatToPeople[hatId].append(personId)

        memo = {}
        targetMask = (1 << numPeople) - 1

        def findWays(currentHatId, assignedPeopleMask):
            if assignedPeopleMask == targetMask:
                return 1

            if currentHatId > 40:
                return 0

            state = (currentHatId, assignedPeopleMask)
            if state in memo:
                return memo[state]

            ways = findWays(currentHatId + 1, assignedPeopleMask)

            for personId in hatToPeople[currentHatId]:
                if not ((assignedPeopleMask >> personId) & 1):
                    newMask = assignedPeopleMask | (1 << personId)
                    ways = (ways + findWays(currentHatId + 1, newMask)) % mod

            memo[state] = ways
            return ways

        return findWays(1, 0)