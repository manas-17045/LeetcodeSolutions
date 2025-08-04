# Leetcode 904: Fruit Into Baskets
# https://leetcode.com/problems/fruit-into-baskets/
# Solved on 4th of August, 2025
class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        """
        Calculates the maximum number of fruits that can be picked from a row of trees
        such that the picked fruits are of at most two types.

        Args:
            fruits: A list of integers representing the type of fruit on each tree.
        Returns:
            The maximum number of fruits that can be picked.
        """
        count = {}          # Maps fruit_type -> its count in the current window
        left = 0            # Left end of our sliding window
        max_picked = 0      # Best windiw size seen so far

        # Expand the window to the right one fruit at a time
        for right, f in enumerate(fruits):
            count[f] = count.get(f, 0) + 1

            # If we have more than 2 types, shrink from the left.
            while len(count) > 2:
                left_fruit = fruits[left]
                count[left_fruit] -= 1
                if count[left_fruit] == 0:
                    del count[left_fruit]
                left += 1

            # Update best window size
            max_picked = max(max_picked, right - left + 1)

        return max_picked