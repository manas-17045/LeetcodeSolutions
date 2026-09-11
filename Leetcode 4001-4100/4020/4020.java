// Leetcode 4020: Elevator Requests I
// https://leetcode.com/problems/elevator-requests-i/
// Solved on 11th of September, 2026
class Solution {
    /**
     * Calculates the total time in seconds required to serve all floor requests
     * in sequential order starting from floor 0.
     *
     * @param n the total number of floors in the building
     * @param requests the sequence of requested floors to visit
     * @return the total time in seconds taken to complete all requests
     */
    public int elevatorRequests(int n, int[] requests) {
        int totalTime = 0;
        int currentFloor = 0;

        for (int targetFloor : requests) {
            totalTime += Math.abs(targetFloor - currentFloor);
            currentFloor = targetFloor;
        }

        return totalTime;
    }
}