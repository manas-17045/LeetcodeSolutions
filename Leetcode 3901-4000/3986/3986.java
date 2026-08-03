// Leetcode 3986: Number of Elapsed Seconds Between Two Lines
// https://leetcode.com/problems/number-of-elapsed-seconds-between-two-lines/
// Solved on 3rd of August, 2026
class Solution {
    /**
     * Calculates the number of elapsed seconds between two given times.
     * 
     * @param startTime The starting time in HH:MM:SS format.
     * @param endTime   The ending time in HH:MM:SS format.
     * @return The number of elapsed seconds between startTime and endTime.
     */
    public int secondsBetweenTimes(String startTime, String endTime) {
        return convertToSeconds(endTime) - convertToSeconds(startTime);
    }

    private int convertToSeconds(String time) {
        int hours = (time.charAt(0) - '0') * 10 + (time.charAt(1) - '0');
        int minutes = (time.charAt(3) - '0') * 10 + (time.charAt(4) - '0');
        int seconds = (time.charAt(6) - '0') * 10 + (time.charAt(7) - '0');
        return hours * 3600 + minutes * 60 + seconds;
    }
}