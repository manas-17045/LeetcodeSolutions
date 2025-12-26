// Leetcode 3733: Minimum Time to Complete all Deliveries
// https://leetcode.com/problems/minimum-time-to-complete-all-deliveries/
// Solved on 26th of December, 2025
class Solution{
    /**
     * Calculates the minimum time required to complete all deliveries.
     * @param d An array representing delivery requirements, where d[0] is for the first type and d[1] for the second.
     * @param r An array representing rates, where r[0] is for the first type and r[1] for the second.
     * @return The minimum time to complete all deliveries.
     */
    public long minimumTime(int[] d, int[] r) {
        long d1 = d[0];
        long d2 = d[1];
        long r1 = r[0];
        long r2 = r[1];

        long low = d1 + d2;
        long high = 10000000000L;
        long ans = high;
        long lcmVal = lcm(r1, r2);

        while (low <= high) {
            long mid = low + (high - low) / 2;
            if (check(mid, d1, d2, r1, r2, lcmVal)) {
                ans = mid;
                high = mid - 1;
            } else {
                low = mid + 1;
            }
        }
        return ans;
    }

    private boolean check(long time, long d1, long d2, long r1, long r2, long lcmVal) {
        long valid1 = time - time / r1;
        long valid2 = time - time / r2;
        long validUnion = time - time / lcmVal;

        return valid1 >= d1 && valid2 >= d2 && validUnion >= (d1 + d2);
    }

    private long gcd(long a, long b) {
        while (b != 0) {
            long temp = b;
            b = a % b;
            a = temp;
        }
        return a;
    }

    private long lcm(long a, long b) {
        if (a == 0 || b == 0) {
            return 0;
        }
        return (a / gcd(a, b)) * b;
    }
}