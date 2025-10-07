# Leetcode 2260: Minimum Consecutive Cards to Pick Up
# https://leetcode.com/problems/minimum-consecutive-cards-to-pick-up/
# Solved on 7th of October, 2025
import math


class Solution:
    def minimumCardPickup(self, cards: list[int]) -> int:
        """
        Finds the minimum number of consecutive cards needed to pick up to have at least one pair of matching cards.

        Args:
            cards: A list of integers representing the values of the cards.

        Returns:
            The minimum number of consecutive cards to pick up, or -1 if no such pair exists.
        """
        lastSeenIndex = {}
        minLength = math.inf

        for index, cardValue in enumerate(cards):
            if cardValue in lastSeenIndex:
                previousIndex = lastSeenIndex[cardValue]
                currentLength = index - previousIndex + 1
                minLength = min(minLength, currentLength)

            lastSeenIndex[cardValue] = index

        return minLength if minLength != math.inf else -1