// Leetcode 3233: Find the Count of Numbers Which Are Not Special
// https://leetcode.com/problems/find-the-count-of-numbers-which-are-not-special/
// Solved on 8th of December, 2025
class Solution {
    /**
     * Finds the count of numbers which are not special within a given range [l, r].
     * A number is considered special if it is a perfect square of a prime number.
     * @param l The lower bound of the range (inclusive).
     * @param r The upper bound of the range (inclusive).
     * @return The count of non-special numbers in the range [l, r].
     */
    public int nonSpecialCount(int l, int r) {
        int limit = (int) Math.sqrt(r);
        boolean[] isComposite = new boolean[limit + 1];
        isComposite[1] = true;

        for (int i = 2; i * i <= limit; i++) {
            if (!isComposite[i]) {
                for (int j = i * i; j <= limit; j += i) {
                    isComposite[j] = true;
                }
            }
        }

        int specialCount = 0;
        for (int i = 2; i <= limit; i++) {
            if (!isComposite[i]) {
                int square = i * i;
                if (square >= l) {
                    specialCount++;
                }
            }
        }

        return r - l + 1 - specialCount;
    }
}