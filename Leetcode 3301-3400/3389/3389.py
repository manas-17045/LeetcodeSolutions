# Leetcode 3389: Minimum Operations to Make Character Frequencies Equal
# https://leetcode.com/problems/minimum-operations-to-make-character-frequencies-unique/
# Solved on 4th of December, 2025
class Solution:
    def makeStringGood(self, s: str) -> int:
        """
        This function calculates the minimum operations to make character frequencies equal.

        Args:
            s (str): The input string.
        Returns:
            int: The minimum number of operations required.
        """
        counts = [0] * 26
        for char in s:
            counts[ord(char) - ord('a')] += 1

        n = len(s)
        minOps = n

        for k in range(1, n + 1):
            prevDrop = counts[0]
            prevKeep = abs(counts[0] - k)

            for i in range(1, 26):
                count = counts[i]

                currDrop = count + min(prevDrop, prevKeep)

                adjust = abs(count - k)
                deficit = max(0, k - count)

                costFromDrop = prevDrop + adjust - min(counts[i - 1], deficit)

                surplus = max(0, counts[i - 1] - k)
                costFromKeep = prevKeep + adjust - min(surplus, deficit)

                currKeep = min(costFromDrop, costFromKeep)

                prevDrop = currDrop
                prevKeep = currKeep

            minOps = min(minOps, prevDrop, prevKeep)

        return minOps