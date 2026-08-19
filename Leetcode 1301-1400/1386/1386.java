// Leetcode 1386: Cinema Seat Allocation
// https://leetcode.com/problems/cinema-seat-allocation/
// Solved on 19th of August, 2026
import java.util.Hashmap;
import java.util.Map;

class Solution {
    /**
     * Calculates the maximum number of 4-person families that can be seated together
     * across n rows of 10-seat aisles, accounting for reserved seats.
     *
     * Valid 4-seat contiguous blocks are: [2, 3, 4, 5], [6, 7, 8, 9], or [4, 5, 6, 7].
     *
     * @param n             The total number of rows in the cinema theater (1-indexed).
     * @param reservedSeats A 2D integer array where each element [row, col] denotes an already booked seat.
     * @return              The maximum number of 4-person family groups that can be accommodated.
     */
    public int maxNumberOfFamilies(int n, int[][] reservedSeats) {
        Map<Integer, Integer> rowReservations = new HashMap<>();
        
        for (int[] seat : reservedSeats) {
            int row = seat[0];
            int col = seat[1];
            if (col >= 2 && col <= 9) {
                rowReservations.put(row, rowReservations.getOrDefault(row, 0) | (1 << col));
            }
        }
        
        int totalGroups = (n - rowReservations.size()) * 2;
        
        for (int mask : rowReservations.values()) {
            boolean left = (mask & 60) == 0;
            boolean right = (mask & 960) == 0;
            boolean middle = (mask & 240) == 0;
            
            if (left && right) {
                totalGroups += 2;
            } else if (left || right || middle) {
                totalGroups += 1;
            }
        }
        
        return totalGroups;
    }
}