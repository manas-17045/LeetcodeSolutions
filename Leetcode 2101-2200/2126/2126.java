// Leetcode 2126: Destroying Asteroids
// https://leetcode.com/problems/destroying-asteroids/
// Solved on 31st of May, 2026
import java.util.Arrays;

class Solution {
    /**
     * Determines if all asteroids can be destroyed by a planet of a given mass.
     * 
     * @param mass The initial mass of the planet.
     * @param asteroids An array of integers representing the mass of each asteroid.
     * @return True if all asteroids can be destroyed, false otherwise.
     */
    public boolean asteroidDestroyed(int mass, int[] asteroids) {
        Arrays.sort(asteroids);
        long currentMass = mass;
        for (int asteroid : asteroids) {
            if (currentMass < asteroid) {
                return false;
            }
            currentMass += asteroid;
        }
        return true;
    }
}