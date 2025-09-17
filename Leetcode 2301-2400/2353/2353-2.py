# Leetcode 2353: Design a Food Rating System
# https://leetcode.com/problems/design-a-food-rating-system/
# Solved on 17th of September, 2025
import heapq
from collections import defaultdict


class FoodRatings:

    def __init__(self, foods: list[str], cuisines: list[str], ratings: list[int]):
        self.food_info = {}
        self.cuisine_heaps = defaultdict(list)

        for f, c, r in zip(foods, cuisines, ratings):
            self.food_info[f] = [r, c]
            heapq.heappush(self.cuisine_heaps[c], (-r, f))

    def changeRating(self, food: str, newRating: int) -> None:
        cuisine, _ = self.food_info[food]
        # Update mapping
        self.food_info[food] = (cuisine, newRating)
        # Push new entry onto the cuisine heap
        heapq.heappush(self.cuisine_heaps[cuisine], (-newRating, food))

    def highestRated(self, cuisine: str) -> str:
        heap = self.cuisine_heaps[cuisine]
        # Pop entries that are stale
        while heap:
            neg_r, food = heap[0]
            current_rating = self.food_info[food][1]
            if -neg_r == current_rating:
                return food
            heapq.heappop(heap)

        # According to constraints, cuisine will always have at least one food.
        return ""