# Leetcode 2126: Destroying Asteroids
# https://leetcode.com/problems/destroying-asteroids/
# Solved on 16th of August, 2025
class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: list[int]) -> bool:
        """
        Determines if all asteroids can be destroyed given an initial mass.

        Args:
            mass (int): The initial mass of the spaceship.
            asteroids (list[int]): A list of integers representing the mass of each asteroid.
        Returns:
            bool: True if all asteroids can be destroyed, False otherwise.
        """
        asteroids.sort()

        currentMass = mass

        for asteroidMass in asteroids:
            if currentMass < asteroidMass:
                return False
            currentMass += asteroidMass

        return True