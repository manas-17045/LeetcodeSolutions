// Leetcode 3848: Check Digitorial Permutation
// https://leetcode.com/problems/check-digitorial-permutation/
// Solved on 24th of February, 2026
class Solution {
    /**
     * Checks if the sum of the factorials of the digits of n is a permutation of n.
     * @param n The integer to check.
     * @return True if the sum of factorials of digits of n is a permutation of n, false otherwise.
     */
    public boolean isDigitorialPermutation(int n) {
        int[] fact = {1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880};
        int sum = 0;
        int temp = n;
        int[] count = new int[10];
        int len1 = 0;

        while (temp > 0) {
            int digit = temp % 10;
            sum += fact[digit];
            count[digit]++;
            len1++;
            temp /= 10;
        }

        temp = sum;
        int len2 = 0;

        while (temp > 0) {
            int digit = temp % 10;
            count[digit]--;
            len2++;
            temp /= 10;
        }

        if (len1 != len2) {
            return false;
        }

        for (int i = 0; i < 10; i++) {
            if (count[i] != 0) {
                return false;
            }
        }

        return true;
    }
}