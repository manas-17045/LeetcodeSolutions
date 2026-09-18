// Leetcode 4025: Minimize the Maximum Waiting Time atSynchronized Traffic Lights
// https://leetcode.com/problems/minimize-the-maximum-waiting-time-at-synchronized-traffic-lights/
// Solved on 18th of September, 2026
class Solution {
    /**
     * Calculates the minimum possible penalty, which is the maximum waiting
     * time experienced by any car when assigned optimally to synchronized
     * traffic lights.
     *
     * @param period the cycle duration in seconds for all traffic lights
     * @param lights an array representing the green phase durations for each light
     * @param arrivalTime an array representing the arrival times of each car
     * @return the minimum possible maximum waiting time among all cars
     */
    public int minPenalty(int period, int[] lights, int[] arrivalTime) {
        int maxGreen = 0;
        for (int light : lights) {
            if (light > maxGreen) {
                maxGreen = light;
            }
        }

        int maxPenalty = 0;
        for (int time : arrivalTime) {
            int remainder = time % period;
            if (remainder >= maxGreen) {
                int waitTime = period - remainder;
                if (waitTime > maxPenalty) {
                    maxPenalty = waitTime;
                }
            }
        }

        return maxPenalty;
    }
}