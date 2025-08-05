# Leetcode 1333: Filter Restaurants by Vegan-Friendly, Price and Distance
# https://leetcode.com/problems/filter-restaurants-by-vegan-friendly-price-and-distance/
# Solved on 5th of August, 2025
class Solution:
    def filterRestaurants(self, restaurants: list[list[int]], veganFriendly: int, maxPrice: int, maxDistance: int) -> list[int]:
        """
        Filters and sorts a list of restaurants based on given criteria.

        Args:
            restaurants (list[list[int]]): A list of restaurant details, where each inner list is [id, rating, veganFriendly, price, distance].
            veganFriendly (int): A flag (1 or 0) indicating whether to filter for vegan-friendly restaurants.
            maxPrice (int): The maximum price allowed.
            maxDistance (int): The maximum distance allowed.
        Returns:
            list[int]: A list of restaurant IDs, sorted by rating (descending) then by ID (descending).
        """
        # Apply all three filters
        filtered = []
        for id_, rating, isVegan, price, dist in restaurants:
            if veganFriendly and isVegan == 0:
                continue
            if price > maxPrice or dist > maxDistance:
                continue
            filtered.append((rating, id_))

        # Sort by rating descending, then id descending
        filtered.sort(key=lambda x: (-x[0], -x[1]))

        # Extract the restaurant IDs in order
        return [id_ for _, id_ in filtered]