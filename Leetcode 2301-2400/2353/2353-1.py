# Leetcode 2353: Design a Food Rating System
# https://leetcode.com/problems/design-a-food-rating-system/
# Solved on 17th of September, 2025
import collections
import heapq


class FoodRatings:

    def __init__(self, foods: list[str], cuisines: list[str], ratings: list[int]):
        self.foodData = {}
        self.cuisineHeaps = collections.defaultdict(list)
        for i in range(len(foods)):
            food = foods[i]
            cuisine = cuisines[i]
            rating = ratings[i]
            self.foodData[food] = [rating, cuisine]
            heapq.heappush(self.cuisineHeaps[cuisine], (-rating, food))

    def changeRating(self, food: str, newRating: int) -> None:
        self.foodData[food][0] = newRating
        cuisine = self.foodData[food][1]
        heapq.heappush(self.cuisineHeaps[cuisine], (-newRating, food))

    def highestRated(self, cuisine: str) -> str:
        cuisineHeap = self.cuisineHeaps[cuisine]
        while True:
            rating, food = cuisineHeap[0]
            if -rating == self.foodData[food][0]:
                return food
            heapq.heappop(cuisineHeap)