// Leetcode 3770: Largest Prime From Consecutive Prime Sum
// https://leetcode.com/problems/largest-prime-from-consecutive-prime-sum/
// Solved on 25th of December, 2025
class Solution {
    /**
     * Given an integer n, find the largest prime number that can be expressed as the sum of consecutive prime numbers,
     * where the sum does not exceed n.
     * @param n The upper limit for the sum of consecutive primes.
     * @return The largest prime number that is a sum of consecutive primes and does not exceed n, or 0 if no such prime exists.
     */
    public int largestPrime(int n) {
        if (n < 2) {
            return 0;
        }
        boolean[] isPrime = new boolean[n + 1];
        for (int i = 2; i <= n; i++) {
            isPrime[i] = true;
        }
        for (int i = 2; i * i <= n; i++) {
            if (isPrime[i]) {
                for (int j = i * i; j <= n; j += i) {
                    isPrime[j] = false;
                }
            }
        }
        int sum = 0;
        int result = 0;
        for (int i = 2; i <= n; i++) {
            if (isPrime[i]) {
                sum += i;
                if (sum > n) {
                    break;
                }
                if (isPrime[sum]) {
                    result = sum;
                }
            }
        }
        return result;
    }
}