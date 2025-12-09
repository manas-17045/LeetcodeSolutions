// Leetcode 3145: Find Products of Elements of Big Array
// https://leetcode.com/problems/find-products-of-elements-of-big-array/
// Solved on 9th of December, 2025
class Solution {
    /**
     * Finds the products of elements for a given set of queries.
     *
     * @param queries A 2D array where each inner array represents a query [startIdx, endIdx, mod].
     * @return An array of integers, where each element is the product for the corresponding query modulo `mod`.
     */
    public int[] findProductsOfElements(long[][] queries) {
        int[] result = new int[queries.length];
        for (int i = 0; i < queries.length; i++) {
            result[i] = solve(queries[i]);
        }
        return result;
    }

    private int solve(long[] query) {
        long startIdx = query[0];
        long endIdx = query[1];
        long mod = query[2];

        if (mod == 1){
            return 0;
        }

        long startNum = getNum(startIdx);
        long endNum = getNum(endIdx);

        long totalPower = 0;

        long prevCountStart = countSetBits(startNum - 1);
        long startOffset = startIdx - prevCountStart;

        if (startNum == endNum) {
            long endOffset = endIdx - prevCountStart;
            totalPower += sumSpecificBits(startNum, startOffset, endOffset);
        } else {
            totalPower += sumSpecificBits(startNum, startOffset, -1);
            if (endNum > startNum + 1) {
                totalPower += sumPowers(endNum - 1) - sumPowers(startNum);
            }
            long prevCountEnd = countSetBits(endNum - 1);
            long endOffset = endIdx - prevCountEnd;
            totalPower += sumSpecificBits(endNum, 0, endOffset);
        }

        return (int) modularExponentiation(2, totalPower, mod);
    }

    private long sumSpecificBits(long num, long startIdx, long endIdx) {
        long sum = 0;
        long count = 0;
        for (int i = 0; i < 60; i++) {
            if ((num & (1L << i)) != 0) {
                if (count >= startIdx && (endIdx == -1 || count <= endIdx)) {
                    sum += i;
                }
                count++;
            }
        }
        return sum;
    }

    private long getNum(long index) {
        long low = 1, high = (long) 1e15;
        long ans = 1;
        while (low <= high) {
            long mid = low + (high - low) / 2;
            if (countSetBits(mid) > index) {
                ans = mid;
                high = mid - 1;
            } else {
                low = mid + 1;
            }
        }
        return ans;
    }

    private long countSetBits(long n) {
        long count = 0;
        for (int i = 0; i < 60; i++) {
            long block = 1L << (i + 1);
            long half = 1L << i;
            long fullCycles = (n + 1) / block;
            count += fullCycles * half;
            long remainder = (n + 1) % block;
            if (remainder > half) {
                count += remainder - half;
            }
        }
        return count;
    }

    private long sumPowers(long n) {
        long totalSum = 0;
        for (int i = 0; i < 60; i++) {
            long block = 1L << (i + 1);
            long half = 1L << i;
            long fullCycles = (n + 1) / block;
            long currCount = fullCycles * half;
            long remainder = (n + 1) % block;
            if (remainder > half) {
                currCount += remainder - half;
            }
            totalSum += currCount * i;
        }
        return totalSum;
    }

    private long modularExponentiation(long base, long exp, long mod) {
        long res = 1;
        base %= mod;
        while (exp > 0) {
            if ((exp % 2) == 1)
                res = (res * base) % mod;
            base = (base * base) % mod;
            exp /= 2;
        }
        return res;
    }
}