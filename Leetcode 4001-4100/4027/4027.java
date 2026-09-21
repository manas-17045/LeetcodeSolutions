// Leetcode 4027: Elevator Requests III
// https://leetcode.com/problems/elevator-requests-iii/
// Solved on 21st of September, 2026
class Solution {
    /**
     * Calculates the minimum time needed to fulfill all elevator requests.
     *
     * @param n the total number of floors in the building
     * @param start the starting floor of the elevator
     * @param requests a 2D array where each element contains the arrival time and the requested floor
     * @return the minimum time required to fulfill all requests
     */
    public long elevatorRequests(int n, int start, int[][] requests) {
        int numRequests = requests.length;
        int totalStates = 1 << numRequests;
        long[][] minTime = new long[totalStates][numRequests];

        for (int mask = 0; mask < totalStates; mask++) {
            for (int i = 0; i < numRequests; i++) {
                minTime[mask][i] = Long.MAX_VALUE;
            }
        }

        for (int i = 0; i < numRequests; i++) {
            long travelDistance = Math.abs(start - requests[i][1]);
            minTime[1 << i][i] = Math.max(travelDistance, requests[i][0]);
        }

        for (int mask = 1; mask < totalStates; mask++) {
            for (int i = 0; i < numRequests; i++) {
                if ((mask & (1 << i)) != 0) {
                    for (int j = 0; j < numRequests; j++) {
                        if (i != j && (mask & (1 << j)) != 0) {
                            long previousTime = minTime[mask ^ (1 << i)][j];
                            if (previousTime != Long.MAX_VALUE) {
                                long travelDistance = Math.abs(requests[i][1] - requests[j][1]);
                                long arrivalTime = requests[i][0];
                                long newTime = Math.max(previousTime + travelDistance, arrivalTime);
                                minTime[mask][i] = Math.min(minTime[mask][i], newTime);
                            }
                        }
                    }
                }
            }
        }

        long result = Long.MAX_VALUE;
        for (int i = 0; i < numRequests; i++) {
            result = Math.min(result, minTime[totalStates - 1][i]);
        }

        return result;
    }
}