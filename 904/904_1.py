# Leetcode 904: Fruit Into Baskets
# https://leetcode.com/problems/fruit-into-baskets/
# Solved on 4th of August, 2025
import collections


class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        """
        Calculates the maximum number of fruits that can be collected into at most two types of baskets.

        Args:
            fruits (list[int]): A list of integers representing the type of fruit in each tree.
        Returns:
            int: The maximum number of fruits that can be collected.
        """
        leftPointer = 0
        maxLength = 0
        fruitFrequency = collections.defaultdict(int)

        for rightPointer, fruit in enumerate(fruits):
            fruitFrequency[fruit] += 1

            while len(fruitFrequency) > 2:
                leftFruit = fruits[leftPointer]
                fruitFrequency[leftFruit] -= 1
                if fruitFrequency[leftFruit] == 0:
                    del fruitFrequency[leftFruit]
                leftPointer += 1

            currentLength = rightPointer - leftPointer + 1
            maxLength = max(maxLength, currentLength)

        return maxLength