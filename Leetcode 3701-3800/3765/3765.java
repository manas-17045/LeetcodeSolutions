// Leetcode 3765: Complete Prime Number
// https://leetcode.com/problems/complete-prime-number/
// Solved on 26th of December, 2025
class Solution {
    /**
     * Checks if a given number is a "complete prime number".
     * A number is a complete prime if all its prefixes and suffixes (when read as numbers) are prime.
     * @param num The integer to check.
     * @return True if the number is a complete prime, false otherwise.
     */
    public boolean completePrime(int num) {
        int temp = num;
        while (temp > 0) {
            if (!isPrime(temp)) {
                return false;
            }
            temp /= 10;
        }

        long mod = 10;
        while (mod < num) {
            if (!isPrime((int) (num % mod))) {
                return false;
            }
            mod *= 10;
        }

        return true;
    }

    private boolean isPrime(int n) {
        if (n <= 1) {
            return false;
        }
        if (n == 2 || n == 3) {
            return true;
        }
        if (n % 2 == 0 || n % 3 == 0) {
            return false;
        }
        for (int i = 5; i * i <= n; i += 6) {
            if (n % i == 0 || n % (i + 2) == 0) {
                return false;
            }
        }
        return true;
    }
}