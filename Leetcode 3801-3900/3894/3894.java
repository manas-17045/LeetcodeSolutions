// Leetcode 3894: Traffic Signal Color
// https://leetcode.com/problems/traffic-signal-color/
// Solved on 19th of April, 2026
class Solution {
    /**
     * Determines the traffic signal color based on the timer value.
     * @param timer The current time value of the signal.
     * @return A string representing the color of the traffic signal.
     */
    public String trafficSignal(int timer) {
        if (timer == 0) {
            return "Green";
        }
        if (timer == 30) {
            return "Orange";
        }
        if (timer > 30 && timer <= 90) {
            return "Red";
        }
        return "Invalid";
    }
}