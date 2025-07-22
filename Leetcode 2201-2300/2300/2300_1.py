# Leetcode 2300: Successful Pairs of Spells and Potions
# https://leetcode.com/problems/successful-pairs-of-spells-and-potions/
# Solved on 22nd of July, 2025
class Solution:
    def successfulPairs(self, spells: list[int], potions: list[int], success: int) -> list[int]:
        """
        Calculates the number of successful pairs for each spell.

        Args:
            spells (list[int]): A list of integers representing the strength of each spell.
            potions (list[int]): A list of integers representing the strength of each potion.
            success (int): The minimum product required for a spell-potion pair to be successful.
        Returns:
            list[int]: A list where each element is the number of successful potion pairs for the corresponding spell.
        """

        potions.sort()

        numPotions = len(potions)
        result = []

        for spellStrength in spells:
            left = 0
            right = numPotions - 1
            firstSuccessIndex = numPotions

            while left <= right:
                mid = left + (right - left) // 2
                product = spellStrength * potions[mid]

                if product >= success:
                    firstSuccessIndex = mid
                    right = mid - 1
                else:
                    left = mid + 1

            count = numPotions - firstSuccessIndex
            result.append(count)

        return result