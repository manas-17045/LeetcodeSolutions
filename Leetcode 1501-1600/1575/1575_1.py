# Leetcode 1575: Count All Possible Routes
# https://leetcode.com/problems/count-all-possible-routes/
# Solved on 13th of July, 2025
class Solution:
    def countRoutes(self, locations: list[int], start: int, finish: int, fuel: int) -> int:
        """
        Counts the number of possible routes from a start city to a finish city
        given a list of city locations and an initial amount of fuel.

        Args:
            locations (list[int]): A list of integers where locations[i] is the position of city i.
            start (int): The index of the starting city.
            finish (int): The index of the finishing city.
            fuel (int): The initial amount of fuel available.

        Returns:
            int: The number of possible routes modulo 10^9 + 7.
        """
        numCities = len(locations)
        mod = 10**9 + 7

        memo = [[-1] * (fuel + 1) for _ in range(numCities)]

        def countPaths(city, currentFuel):
            if memo[city][currentFuel] != -1:
                return memo[city][currentFuel]

            paths = 0
            if city == finish:
                paths = 1

            for nextCity in range(numCities):
                if city == nextCity:
                    continue

                fuelCost = abs(locations[city] - locations[nextCity])

                if currentFuel >= fuelCost:
                    paths = (paths + countPaths(nextCity, currentFuel - fuelCost)) % mod

            memo[city][currentFuel] = paths
            return paths

        return countPaths(start, fuel)