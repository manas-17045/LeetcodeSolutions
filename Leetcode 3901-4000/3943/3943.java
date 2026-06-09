// Leetcode 3943: Number of Pairs After Increment
// https://leetcode.com/problems/number-of-pairs-after-increment/
// Solved on 9th of June, 2026
class Solution {
    static class BlockMap {
        long[] keys;
        int[] values;
        int mask;
        
        public BlockMap(int cap) {
            int c = 1;
            while (c < cap) {
                c <<= 1;
            }
            keys = new long[c];
            values = new int[c];
            mask = c - 1;
        }
        
        public void clear() {
            for (int i = 0; i <= mask; i++) {
                keys[i] = 0;
                values[i] = 0;
            }
        }
        
        public void add(long k) {
            int pos = (int) (hash(k) & mask);
            while (keys[pos] != 0 && keys[pos] != k) {
                pos = (pos + 1) & mask;
            }
            keys[pos] = k;
            values[pos]++;
        }
        
        public int get(long k) {
            int pos = (int) (hash(k) & mask);
            while (keys[pos] != 0) {
                if (keys[pos] == k) {
                    return values[pos];
                }
                pos = (pos + 1) & mask;
            }
            return 0;
        }
        
        private long hash(long k) {
            k ^= k >>> 33;
            k *= 0xff51afd7ed558ccdL;
            k ^= k >>> 33;
            return k;
        }
    }

    /**
     * Calculates the number of pairs (i, j) such that nums1[i] + nums2[j] equals a target value
     * after performing range increment updates on nums2.
     * @param nums1 The first array of integers.
     * @param nums2 The second array of integers, which is subject to range updates.
     * @param queries A 2D array where queries[i][0] is the type (1 for update, 2 for query).
     * @return An array containing the results for each type 2 query.
     */
    public int[] numberOfPairs(int[] nums1, int[] nums2, int[][] queries) {
        int uniqueCount = 0;
        int[] uniqueNums1 = new int[nums1.length];
        int[] countsNums1 = new int[nums1.length];
        
        for (int i = 0; i < nums1.length; i++) {
            boolean found = false;
            for (int j = 0; j < uniqueCount; j++) {
                if (uniqueNums1[j] == nums1[i]) {
                    countsNums1[j]++;
                    found = true;
                    break;
                }
            }
            if (!found) {
                uniqueNums1[uniqueCount] = nums1[i];
                countsNums1[uniqueCount] = 1;
                uniqueCount++;
            }
        }

        int n = nums2.length;
        int blockSize = (int) Math.sqrt(n) + 1;
        int numBlocks = (n + blockSize - 1) / blockSize;

        long[] arr = new long[n];
        long[] lazy = new long[numBlocks];
        BlockMap[] maps = new BlockMap[numBlocks];

        for (int i = 0; i < numBlocks; i++) {
            maps[i] = new BlockMap(blockSize * 2);
        }

        for (int i = 0; i < n; i++) {
            arr[i] = nums2[i];
            int b = i / blockSize;
            maps[b].add(arr[i]);
        }

        int resSize = 0;
        for (int i = 0; i < queries.length; i++) {
            if (queries[i][0] == 2) {
                resSize++;
            }
        }

        int[] ans = new int[resSize];
        int qIdx = 0;

        for (int i = 0; i < queries.length; i++) {
            int[] q = queries[i];
            
            if (q[0] == 1) {
                int x = q[1];
                int y = q[2];
                long val = q[3];
                int startBlock = x / blockSize;
                int endBlock = y / blockSize;

                if (startBlock == endBlock) {
                    for (int j = x; j <= y; j++) {
                        arr[j] += val;
                    }
                    maps[startBlock].clear();
                    int bStart = startBlock * blockSize;
                    int bEnd = Math.min(n, bStart + blockSize);
                    for (int j = bStart; j < bEnd; j++) {
                        maps[startBlock].add(arr[j]);
                    }
                } else {
                    int bStartLimit = Math.min(n, (startBlock + 1) * blockSize);
                    for (int j = x; j < bStartLimit; j++) {
                        arr[j] += val;
                    }
                    maps[startBlock].clear();
                    int bStart = startBlock * blockSize;
                    for (int j = bStart; j < bStartLimit; j++) {
                        maps[startBlock].add(arr[j]);
                    }

                    for (int b = startBlock + 1; b < endBlock; b++) {
                        lazy[b] += val;
                    }

                    int endStart = endBlock * blockSize;
                    for (int j = endStart; j <= y; j++) {
                        arr[j] += val;
                    }
                    maps[endBlock].clear();
                    int bEndMax = Math.min(n, endStart + blockSize);
                    for (int j = endStart; j < bEndMax; j++) {
                        maps[endBlock].add(arr[j]);
                    }
                }
            } else {
                long tot = q[1];
                int pairs = 0;
                
                for (int j = 0; j < uniqueCount; j++) {
                    long targetBase = tot - uniqueNums1[j];
                    for (int b = 0; b < numBlocks; b++) {
                        long target = targetBase - lazy[b];
                        pairs += countsNums1[j] * maps[b].get(target);
                    }
                }
                ans[qIdx++] = pairs;
            }
        }
        
        return ans;
    }
}