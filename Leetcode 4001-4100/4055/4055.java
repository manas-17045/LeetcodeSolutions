// Leetcode 4055: Count Shadow Pairs II
// https://leetcode.com/problems/count-shadow-pairs-ii/
// Solved on 22nd of October, 2026
import java.util.Arrays;

class Solution {
    /**
     * Counts the total number of shadow pairs in the given array using bottom-up
     * divide and conquer combined with coordinate compression and a Fenwick tree.
     *
     * @param nums the input array of integers
     * @return the total number of valid shadow pairs
     */
    public int shadowPairs(int[] nums) {
        int n = nums.length;
        int[] sortedNums = nums.clone();
        Arrays.sort(sortedNums);
        int uniqueCount = 0;
        for (int i = 0; i < n; i++) {
            if (i == 0 || sortedNums[i] != sortedNums[i - 1]) {
                sortedNums[uniqueCount++] = sortedNums[i];
            }
        }

        int[] ranks = new int[n];
        for (int i = 0; i < n; i++) {
            ranks[i] = Arrays.binarySearch(sortedNums, 0, uniqueCount, nums[i]) + 1;
        }

        int[] bit = new int[uniqueCount + 1];
        int[] leftVals = new int[n];
        long[] removals = new long[n];
        long[] queries = new long[n];
        int totalPairs = 0;

        for (int step = 1; step < n; step <<= 1) {
            for (int left = 0; left + step < n; left += step << 1) {
                int mid = left + step - 1;
                int right = Math.min(n - 1, left + (step << 1) - 1);
                int leftLen = mid - left + 1;
                int rightLen = right - mid;

                for (int i = mid; i >= left; i--) {
                    int val = ranks[i];
                    int revVal = uniqueCount - val + 1;
                    int bestRev = 0;
                    for (int idx = revVal - 1; idx > 0; idx -= idx & -idx) {
                        if (bit[idx] > bestRev) {
                            bestRev = bit[idx];
                        }
                    }
                    int nextGreater = (bestRev == 0) ? (uniqueCount + 1) : (uniqueCount - bestRev + 1);
                    int pos = i - left;
                    leftVals[pos] = val;
                    removals[pos] = (((long) nextGreater) << 32) | (val & 0xFFFFFFFFL);
                    for (int idx = revVal; idx <= uniqueCount; idx += idx & -idx) {
                        if (revVal > bit[idx]) {
                            bit[idx] = revVal;
                        }
                    }
                }

                for (int i = left; i <= mid; i++) {
                    int revVal = uniqueCount - ranks[i] + 1;
                    for (int idx = revVal; idx <= uniqueCount; idx += idx & -idx) {
                        bit[idx] = 0;
                    }
                }

                for (int j = mid + 1; j <= right; j++) {
                    int val = ranks[j];
                    int prevSmaller = 0;
                    for (int idx = val - 1; idx > 0; idx -= idx & -idx) {
                        if (bit[idx] > prevSmaller) {
                            prevSmaller = bit[idx];
                        }
                    }
                    queries[j - mid - 1] = (((long) val) << 32) | (prevSmaller & 0xFFFFFFFFL);
                    for (int idx = val; idx <= uniqueCount; idx += idx & -idx) {
                        if (val > bit[idx]) {
                            bit[idx] = val;
                        }
                    }
                }

                for (int j = mid + 1; j <= right; j++) {
                    for (int idx = ranks[j]; idx <= uniqueCount; idx += idx & -idx) {
                        bit[idx] = 0;
                    }
                }

                Arrays.sort(leftVals, 0, leftLen);
                Arrays.sort(removals, 0, leftLen);
                Arrays.sort(queries, 0, rightLen);

                int insPtr = 0;
                int remPtr = 0;
                int activeCount = 0;

                for (int q = 0; q < rightLen; q++) {
                    long query = queries[q];
                    int rightVal = (int) (query >>> 32);
                    int lowerBound = (int) query;

                    while (insPtr < leftLen && leftVals[insPtr] < rightVal) {
                        int val = leftVals[insPtr++];
                        for (int idx = val; idx <= uniqueCount; idx += idx & -idx) {
                            bit[idx]++;
                        }
                        activeCount++;
                    }

                    while (remPtr < leftLen && (int) (removals[remPtr] >>> 32) < rightVal) {
                        int val = (int) removals[remPtr++];
                        for (int idx = val; idx <= uniqueCount; idx += idx & -idx) {
                            bit[idx]--;
                        }
                        activeCount--;
                    }

                    int invalidCount = 0;
                    for (int idx = lowerBound - 1; idx > 0; idx -= idx & -idx) {
                        invalidCount += bit[idx];
                    }
                    totalPairs += activeCount - invalidCount;
                }

                for (int k = 0; k < insPtr; k++) {
                    for (int idx = leftVals[k]; idx <= uniqueCount; idx += idx & -idx) {
                        bit[idx] = 0;
                    }
                }
            }
        }

        return totalPairs;
    }
}