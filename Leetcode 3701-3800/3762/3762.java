// Leetcode 3762: Minimum Operations to Equalize Subarrays
// https://leetcode.com/problems/minimum-operations-to-equalize-subarrays/
// Solved on 22nd of December, 2025
import java.util.Arrays;

class Solution {
    /**
     * Calculates the minimum operations to equalize subarrays for a given set of queries.
     * @param nums The input array of integers.
     * @param k The divisor for calculating remainders and values.
     * @param queries A 2D array where each query is [left, right] representing a subarray.
     * @return An array of long integers, where each element is the minimum operations for the corresponding query, or -1 if equalization is not possible.
     */
    public long[] minOperations(int[] nums, int k, int[][] queries) {
        int n = nums.length;
        int m = queries.length;
        long[] ans = new long[m];

        int[] rems = new int[n];
        for (int i = 0; i < n; i++) {
            rems[i] = nums[i] % k;
        }

        int[] diffPrefix = new int[n];
        for (int i = 1; i < n; i++) {
            diffPrefix[i] = diffPrefix[i - 1] + (rems[i] != rems[i - 1] ? 1 : 0);
        }

        long[] vals = new long[n];
        for (int i = 0; i < n; i++) {
            vals[i] = nums[i] / k;
        }

        long[] sortedVals = vals.clone();
        Arrays.sort(sortedVals);
        
        int uniqueCount = 0;
        for (int i = 0; i < n; i++) {
            if (i == 0 || sortedVals[i] != sortedVals[i - 1]) {
                sortedVals[uniqueCount++] = sortedVals[i];
            }
        }

        int[] ranks = new int[n];
        for (int i = 0; i < n; i++) {
            ranks[i] = lowerBound(sortedVals, uniqueCount, vals[i]) + 1;
        }

        int blockSize = (int) Math.sqrt(n);
        Integer[] qIndices = new Integer[m];
        for (int i = 0; i < m; i++) {
            qIndices[i] = i;
        }

        Arrays.sort(qIndices, (a, b) -> {
            int blockA = queries[a][0] / blockSize;
            int blockB = queries[b][0] / blockSize;
            if (blockA != blockB) {
                return blockA - blockB;
            }
            return (blockA % 2 == 0) ? (queries[a][1] - queries[b][1]) : (queries[b][1] - queries[a][1]);
        });

        long[] bitSum = new long[uniqueCount + 1];
        int[] bitCount = new int[uniqueCount + 1];
        int l = 0;
        int r = -1;

        for (int idx : qIndices) {
            int qL = queries[idx][0];
            int qR = queries[idx][1];

            int rangeDiff = 0;
            if (qL < qR) {
                rangeDiff = diffPrefix[qR] - diffPrefix[qL];
            }

            if (rangeDiff > 0) {
                ans[idx] = -1;
                continue;
            }

            while (r < qR) {
                r++;
                add(ranks[r], vals[r], bitCount, bitSum, uniqueCount);
            }
            while (l > qL) {
                l--;
                add(ranks[l], vals[l], bitCount, bitSum, uniqueCount);
            }
            while (r > qR) {
                remove(ranks[r], vals[r], bitCount, bitSum, uniqueCount);
                r--;
            }
            while (l < qL) {
                remove(ranks[l], vals[l], bitCount, bitSum, uniqueCount);
                l++;
            }

            int count = qR - qL + 1;
            int medianRank = (count + 1) / 2;
            int medianBitIdx = findKthIndex(bitCount, uniqueCount, medianRank);
            long medianVal = sortedVals[medianBitIdx - 1];

            long sumSmall = querySum(bitSum, medianBitIdx);
            long cntSmall = queryCount(bitCount, medianBitIdx);
            
            long totalSum = querySum(bitSum, uniqueCount);
            long totalCnt = queryCount(bitCount, uniqueCount);

            long cost = (cntSmall * medianVal - sumSmall) + ((totalSum - sumSmall) - (totalCnt - cntSmall) * medianVal);
            ans[idx] = cost;
        }

        return ans;
    }

    private int lowerBound(long[] arr, int len, long val) {
        int l = 0, r = len;
        while (l < r) {
            int mid = (l + r) / 2;
            if (arr[mid] >= val) {
                r = mid;
            } else {
                l = mid + 1;
            }
        }
        return l;
    }

    private void add(int idx, long val, int[] bitCount, long[] bitSum, int max) {
        for (; idx <= max; idx += idx & -idx) {
            bitCount[idx]++;
            bitSum[idx] += val;
        }
    }

    private void remove(int idx, long val, int[] bitCount, long[] bitSum, int max) {
        for (; idx <= max; idx += idx & -idx) {
            bitCount[idx]--;
            bitSum[idx] -= val;
        }
    }

    private long querySum(long[] bit, int idx) {
        long sum = 0;
        for (; idx > 0; idx -= idx & -idx) {
            sum += bit[idx];
        }
        return sum;
    }

    private int queryCount(int[] bit, int idx) {
        int sum = 0;
        for (; idx > 0; idx -= idx & -idx) {
            sum += bit[idx];
        }
        return sum;
    }

    private int findKthIndex(int[] bitCount, int max, int k) {
        int idx = 0;
        int currentCount = 0;
        int maxPow2 = Integer.highestOneBit(max);
        
        for (int i = maxPow2; i > 0; i >>= 1) {
            if (idx + i <= max && currentCount + bitCount[idx + i] < k) {
                idx += i;
                currentCount += bitCount[idx];
            }
        }
        return idx + 1;
    }
}