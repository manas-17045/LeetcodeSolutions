# Leetcode 3301: Maximize the Total Height of Unique Towers
# https://leetcode.com/problems/maximize-the-total-height-of-the-unique-towers/
# Solved on 3rd of September, 2025
class Solution:
    def maximumTotalSum(self, maximumHeight: list[int]) -> int:
        """
        Calculates the maximum possible total sum of unique heights that can be assigned.

        Args:
            maximumHeight (list[int]): A list of integers representing the maximum allowed height for each position.
        Returns:
            int: The maximum total sum of unique heights, or -1 if it's not possible to assign positive unique heights.
        """
        # Sort in descending order so we can give largest possible unique heights greedily
        maximumHeight.sort(reverse=True)

        total = 0
        prev = 10 ** 18  # large initial previous assigned height
        for h in maximumHeight:
            # Assign the largest allowed value that's strictly less than prev (to keep uniqueness)
            assign = min(h, prev - 1)
            if assign <= 0:
                return -1

            total += assign
            prev = assign

        return total