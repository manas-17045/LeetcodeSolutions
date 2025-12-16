// Leetcode 3509: Maximum Product of Subsequences With an Alternating SUm Equal to K
// https://leetcode.com/problems/maximum-product-of-subsequences-with-an-alternating-sum-equal-to-k/
// Solved on 16th of December, 2025
import java.util.Arrays;

class Solution {
    /**
     * Calculates the maximum product of subsequences with an alternating sum equal to k.
     *
     * @param nums An array of integers.
     * @param k The target alternating sum.
     * @param limit The maximum product value to consider.
     * @return The maximum product found, or -1 if no such subsequence exists.
     */
    public int maxProduct(int[] nums, int k, int limit) {
        int maxPossibleSum = 0;
        for (int x : nums) {
            maxPossibleSum += x;
        }

        if (Math.abs(k) > maxPossibleSum) {
            return -1;
        }

        int offset = 2500;
        int width = 80;

        long[][] dpEven = new long[limit + 1][width];
        long[][] dpOdd = new long[limit + 1][width];

        long[] zeroEven = new long[width];
        long[] zeroOdd = new long[width];

        long[] allEven = new long[width];
        long[] allOdd = new long[width];

        long[] tmpEven = new long[width];
        long[] tmpOdd = new long[width];

        for (int x : nums) {
            if (x == 0) {
                Arrays.fill(tmpEven, 0);
                Arrays.fill(tmpOdd, 0);

                orArrays(tmpEven, zeroOdd, width);
                orArrays(tmpOdd, zeroEven, width);

                orArrays(tmpEven, allOdd, width);
                orArrays(tmpOdd, allEven, width);

                setBit(tmpOdd, offset);

                orArrays(zeroEven, tmpEven, width);
                orArrays(zeroOdd, tmpOdd, width);

            } else {
                for (int p = limit / x; p >= 1; p--) {
                    int np = p * x;

                    shiftLeftAndOr(dpEven[p], dpOdd[np], x, width);
                    shiftRightAndOr(dpOdd[p], dpEven[np], x, width);
                }

                if (x <= limit) {
                    setBit(dpOdd[x], x + offset);
                }

                Arrays.fill(tmpEven, 0);
                Arrays.fill(tmpOdd, 0);

                shiftLeftAndOr(zeroEven, tmpOdd, x, width);
                shiftRightAndOr(zeroOdd, tmpEven, x, width);

                orArrays(zeroEven, tmpEven, width);
                orArrays(zeroOdd, tmpOdd, width);

                Arrays.fill(tmpEven, 0);
                Arrays.fill(tmpOdd, 0);

                shiftLeftAndOr(allEven, tmpOdd, x, width);
                shiftRightAndOr(allOdd, tmpEven, x, width);

                orArrays(allEven, tmpEven, width);
                orArrays(allOdd, tmpOdd, width);

                setBit(allOdd, x + offset);
            }
        }

        int targetBit = k + offset;
        if (targetBit < 0 || targetBit >= width * 64) {
            return -1;
        }

        for (int p = limit; p >= 1; p--) {
            if (checkBit(dpEven[p], targetBit) || checkBit(dpOdd[p], targetBit)) {
                return p;
            }
        }

        if (checkBit(zeroEven, targetBit) || checkBit(zeroOdd, targetBit)) {
            return 0;
        }

        return -1;
    }

    private void orArrays(long[] dest, long[] src, int width) {
        for (int i = 0; i < width; i++) {
            dest[i] |= src[i];
        }
    }

    private void setBit(long[] arr, int bitIndex) {
        arr[bitIndex / 64] |= (1L << (bitIndex % 64));
    }

    private boolean checkBit(long[] arr, int bitIndex) {
        return (arr[bitIndex / 64] & (1L << (bitIndex % 64))) != 0;
    }

    private void shiftLeftAndOr(long[] src, long[] dest, int k, int width) {
        long carry = 0;
        int shiftInv = 64 - k;
        for (int i = 0; i < width; i++) {
            long val = src[i];
            long res = (val << k) | carry;
            carry = val >>> shiftInv;
            dest[i] |= res;
        }
    }

    private void shiftRightAndOr(long[] src, long[] dest, int k, int width) {
        long carry = 0;
        int shiftInv = 64 - k;
        for (int i = width - 1; i >= 0; i--) {
            long val = src[i];
            long res = (val >>> k) | carry;
            carry = val << shiftInv;
            dest[i] |= res;
        }
    }
}