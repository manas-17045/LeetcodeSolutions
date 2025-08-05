# Leetcode 1333: Filter Restaurants by Vegan-Friendly, Price and Distance
# https://leetcode.com/problems/filter-restaurants-by-vegan-friendly-price-and-distance/
# Solved on 5th of August, 2025
class Solution:
    def filterRestaurants(self, restaurants: list[list[int]], veganFriendly: int, maxPrice: int, maxDistance: int) -> list[int]:
        """
        Filters a list of restaurants based on specified criteria and returns their IDs sorted by rating and then by ID.

        Args:
            restaurants (list[list[int]]): A list of restaurants, where each restaurant is represented as [id, rating, veganFriendly, price, distance].
            veganFriendly (int): A flag indicating whether to filter for vegan-friendly restaurants (1 for yes, 0 for no).
            maxPrice (int): The maximum price allowed for a restaurant.
            maxDistance (int): The maximum distance allowed for a restaurant.

        Returns:
            list[int]: A list of IDs of the filtered restaurants, sorted in descending order by rating, then by ID.
        """
        filteredList = []
        for restaurantData in restaurants:
            passesVeganFilter = (veganFriendly == 0) or (restaurantData[2] == 1)
            passesPriceFilter = restaurantData[3] <= maxPrice
            passesDistanceFilter = restaurantData[4] <= maxDistance

            if passesVeganFilter and passesPriceFilter and passesDistanceFilter:
                filteredList.append(restaurantData)

        filteredList.sort(key=lambda r: (r[1], r[0]), reverse=True)

        resultIds = [r[0] for r in filteredList]

        return resultIds