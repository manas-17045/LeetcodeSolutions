# Leetcode 2260: Minimum Consecutive Cards to Pick Up
# https://leetcode.com/problems/minimum-consecutive-cards-to-pick-up/
# Solved on 7th of October, 2025
class Solution:
    def minimumCardPickup(self, cards: list[int]) -> int:
        """
        Given an integer array cards, find the minimum number of cards you have to pick up
        to have at least one pair of matching cards. If no such pair exists, return -1.
        :param cards: A list of integers representing the cards.
        :return: The minimum number of cards to pick up to have a matching pair, or -1 if no such pair exists.
        """
        # Dictionary to store the last index where each card value was seen
        last_seen = {}
        min_pickup = float('inf')

        for i, card in enumerate(cards):
            if card in last_seen:
                # Calculate the number of cards between the two matching cards
                # including both endpoints
                pickup_count = i - last_seen[card] + 1
                min_pickup = min(min_pickup, pickup_count)

            # Update the last seen position for this card value
            last_seen[card] = i

        # If no matching pair was found, return -1
        return min_pickup if min_pickup != float('inf') else -1