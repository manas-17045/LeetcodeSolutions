# Leetcode 2300: Successful Pairs of Spells and Potions
# https://leetcode.com/problems/successful-pairs-of-spells-and-potions/
# Solved on 22nd of July, 2025
import bisect


class Solution:
    def successfulPairs(self, spells: list[int], potions: list[int], success: int) -> list[int]:
        """
        Calculates the number of successful pairs for each spell.
        :param spells: A list of integers representing the strength of each spell.
        :param potions: A list of integers representing the strength of each potion.
        :param success: An integer representing the minimum product required for a successful pair.
        :return: A list of integers, where each element is the number of successful potion pairs for the corresponding spell.
        """
        # Sort potions so that we can binary-search on them
        potions.sort()
        m = len(potions)
        ans = []

        for spell in spells:
            # Compute threshold = ceil(success / spell)
            threshold = (success + spell - 1) // spell

            # Find leftmost index in potions where value >= threshold
            idx = bisect.bisect_left(potions, threshold)

            # All potions from idx...(m - 1) work
            ans.append(m - idx)

        return ans