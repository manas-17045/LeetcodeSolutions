// Leetcode 3881: Direction Assignments with Exactly K Visible People
// https://leetcode.com/problems/direction-assignments-with-exactly-k-visible-people/
// Solved on 1st of April, 2026
class Solution {
    /**
     * Calculates the number of ways to assign directions such that exactly k people are visible.
     *
     * @param n   The total number of people.
     * @param pos The position of the observer.
     * @param k   The required number of visible people.
     * @return    The total count of valid direction assignments modulo 10^9 + 7.
     */
    public int countVisiblePeople(int n, int pos, int k) {
        if (k > n - 1) {
            return 0;
        }
        int moduloValue = 1000000007;
        int limit = Math.min(k, n - 1 - k);
        long numerator = 1;
        long denominator = 1;
        for (int i = 0; i < limit; i++) {
            numerator = (numerator * (n - 1 - i)) % moduloValue;
            denominator = (denominator * (i + 1)) % moduloValue;
        }
        long combinations = (numerator * calculatePower(denominator, moduloValue - 2, moduloValue)) % moduloValue;
        return (int) ((combinations * 2) % moduloValue);
    }

    private long calculatePower(long base, long exponent, int moduloValue) {
        long result = 1;
        base %= moduloValue;
        while (exponent > 0) {
            if ((exponent & 1) == 1) {
                result = (result * base) % moduloValue;
            }
            base = (base * base) % moduloValue;
            exponent >>= 1;
        }
        return result;
    }
}