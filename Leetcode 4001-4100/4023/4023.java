// Leetcode 4023: Elevator Requests II
// https://leetcode.com/problems/elevator-requests-ii/
// Solved on 14th of Septemeber, 2026
import java.util.Arrays;

class Solution {
    /**
     * Calculates the minimum total penalty required to fulfill all elevator requests.
     * The penalty increases by one for each second a request remains unfulfilled.
     * The solution uses interval dynamic programming with space optimization to minimize the cumulative cost.
     *
     * @param n        the total number of floors in the building
     * @param start    the floor where the elevator begins
     * @param requests an array of distinct requested floors
     * @return the minimum total penalty to fulfill all requests
     */
    public long elevatorRequests(int n, int start, int[] requests) {
        boolean startInReq = false;
        for (int req : requests) {
            if (req == start) {
                startInReq = true;
                break;
            }
        }

        int len = startInReq ? requests.length : requests.length + 1;
        int[] arr = new int[len];
        for (int i = 0; i < requests.length; i++) {
            arr[i] = requests[i];
        }
        if (!startInReq) {
            arr[len - 1] = start;
        }

        Arrays.sort(arr);

        int[] pref = new int[len];
        for (int i = 0; i < len; i++) {
            int weight = (arr[i] == start && !startInReq) ? 0 : 1;
            pref[i] = weight + (i > 0 ? pref[i - 1] : 0);
        }

        int startIdx = Arrays.binarySearch(arr, start);
        int totalReq = requests.length;

        long[][] largerDp = new long[len][2];
        for (int i = 0; i < len; i++) {
            largerDp[i][0] = Long.MAX_VALUE;
            largerDp[i][1] = Long.MAX_VALUE;
        }
        largerDp[0][0] = 0;
        largerDp[0][1] = 0;

        for (int sz = len - 1; sz >= 1; sz--) {
            long[][] currDp = new long[len][2];
            for (int i = 0; i < len; i++) {
                currDp[i][0] = Long.MAX_VALUE;
                currDp[i][1] = Long.MAX_VALUE;
            }

            for (int l = 0; l <= len - sz; l++) {
                int r = l + sz - 1;
                int fulfilled = pref[r] - (l > 0 ? pref[l - 1] : 0);
                int rem = totalReq - fulfilled;

                if (l > 0 && largerDp[l - 1][0] != Long.MAX_VALUE) {
                    long dist = arr[l] - arr[l - 1];
                    currDp[l][0] = Math.min(currDp[l][0], largerDp[l - 1][0] + (long) rem * dist);
                }
                if (r < len - 1 && largerDp[l][1] != Long.MAX_VALUE) {
                    long dist = arr[r + 1] - arr[l];
                    currDp[l][0] = Math.min(currDp[l][0], largerDp[l][1] + (long) rem * dist);
                }

                if (l > 0 && largerDp[l - 1][0] != Long.MAX_VALUE) {
                    long dist = arr[r] - arr[l - 1];
                    currDp[l][1] = Math.min(currDp[l][1], largerDp[l - 1][0] + (long) rem * dist);
                }
                if (r < len - 1 && largerDp[l][1] != Long.MAX_VALUE) {
                    long dist = arr[r + 1] - arr[r];
                    currDp[l][1] = Math.min(currDp[l][1], largerDp[l][1] + (long) rem * dist);
                }
            }
            largerDp = currDp;
        }

        return largerDp[startIdx][0];
    }
}