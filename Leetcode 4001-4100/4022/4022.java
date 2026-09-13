// Leetcode 4022: K-th Digit in Infinite String
// https://leetcode.com/problems/k-th-digit-in-infinite-string/
// Solved on 13th of September, 2026
class Solution {
    /**
     * Finds the k-th digit in the infinite string formed by appending integers
     * in alternating increasing and decreasing blocks of ten.
     *
     * @param k the 1-indexed position of the desired digit
     * @return the digit at the k-th position
     */
    public int kthDigit(long k) {
        if (k <= 9) {
            return (int) k;
        }

        long low = 0;
        long high = k;
        long block = high;

        while (low <= high) {
            long mid = low + (high - low) / 2;
            if (countDigits(10 * mid + 9) >= k) {
                block = mid;
                high = mid - 1;
            } else {
                low = mid + 1;
            }
        }

        long prevDigits = countDigits(10 * block - 1);
        long rem = k - prevDigits;
        long index = rem - 1;

        long startNum = 10 * block;
        int digitLen = 0;
        long temp = startNum;
        while (temp > 0) {
            digitLen++;
            temp /= 10;
        }

        long numIdx = index / digitLen;
        long digitIdx = index % digitLen;

        long targetNum;
        if (block % 2 == 0) {
            targetNum = 10 * block + numIdx;
        } else {
            targetNum = 10 * block + 9 - numIdx;
        }

        long divisor = 1;
        for (int i = 0; i < digitLen - 1 - digitIdx; i++) {
            divisor *= 10;
        }

        return (int) ((targetNum / divisor) % 10);
    }

    private long countDigits(long n) {
        if (n <= 0) {
            return 0;
        }
        long total = 0;
        long start = 1;
        long len = 1;
        while (start <= n) {
            long end = Math.min(n, start * 10 - 1);
            total += (end - start + 1) * len;
            if (start > Long.MAX_VALUE / 10) {
                break;
            }
            start *= 10;
            len++;
        }
        return total;
    }
}