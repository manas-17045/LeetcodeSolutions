# Leetcode 2126: Destroying Asteroids
# https://leetcode.com/problems/destroying-asteroids/
# Solved on 16th of August, 2025
class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: list[int]) -> bool:
        """
        Determines if all asteroids can be destroyed.
        Args:
            mass (int): The initial mass of the spaceship.
            asteroids (list[int]): A list of asteroid masses.
        Returns:
            bool: True if all asteroids can be destroyed, False otherwise.
        """
        # Eat smaller asteroids first to grow as quickly as possible.
        asteroids.sort()
        cur = mass
        for a in asteroids:
            if cur < a:
                return False
            cur += a
        return True