// Leetcode 401: Binary Watch
// https://leetcode.com/problems/binary-watch/
// Solved on 17th of February, 2026
import java.util.ArrayList;
import java.util.List;

class Solution {
    /**
     * Returns all possible times the watch could represent based on the number of LEDs turned on.
     *
     * @param turnedOn The number of LEDs that are currently on.
     * @param return A list of strings representing the possible times in "h:mm" format.
     */
    public List<String> readBinaryWatch(int turnedOn) {
        List<String> times = new ArrayList<>();
        for (int hour = 0; hour < 12; hour++) {
            for (int minute = 0; minute < 60; minute++) {
                if (Integer.bitCount(hour) + Integer.bitCount(minute) == turnedOn) {
                    times.add(hour + ":" + (minute < 10 ? "0" : "") + minute);
                }
            }
        }
        return times;
    }
}