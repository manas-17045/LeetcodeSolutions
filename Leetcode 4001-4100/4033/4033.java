// Leetcode 4033: Valid K-Unique Subarrays I
// https://leetcode.com/problems/valid-k-unique-subarrays-i/
// Solved on 25th of September, 2026
import java.util.Arrays;

class Solution {
    /**
     * Evaluates whether each queried subarray contains exactly k distinct numbers,
     * with every number in the subarray appearing an even number of times.
     *
     * @param nums    the input array of integers
     * @param k       the required number of distinct elements
     * @param queries the 2D array of queries where each query provides the left and right bounds
     * @return a boolean array where each element indicates the validity of the corresponding query
     */
    public boolean[] validSubarrays(int[] nums, int k, int[][] queries) {
        int numQueries = queries.length;
        boolean[] ans = new boolean[numQueries];
        int blockSize = (int) Math.sqrt(nums.length);
        if (blockSize == 0) {
            blockSize = 1;
        }

        int[][] sortedQueries = new int[numQueries][4];
        for (int i = 0; i < numQueries; i++) {
            sortedQueries[i][0] = queries[i][0];
            sortedQueries[i][1] = queries[i][1];
            sortedQueries[i][2] = i;
            sortedQueries[i][3] = queries[i][0] / blockSize;
        }

        Arrays.sort(sortedQueries, (a, b) -> {
            if (a[3] != b[3]) {
                return Integer.compare(a[3], b[3]);
            }
            return (a[3] % 2 == 1) ? Integer.compare(a[1], b[1]) : Integer.compare(b[1], a[1]);
        });

        int[] frequencies = new int[100005];
        int currentL = 0;
        int currentR = -1;
        int distinctCount = 0;
        int oddCount = 0;

        for (int i = 0; i < numQueries; i++) {
            int left = sortedQueries[i][0];
            int right = sortedQueries[i][1];
            int originalIndex = sortedQueries[i][2];

            while (currentL > left) {
                currentL--;
                int val = nums[currentL];
                if (frequencies[val] == 0) {
                    distinctCount++;
                }
                frequencies[val]++;
                if (frequencies[val] % 2 != 0) {
                    oddCount++;
                } else {
                    oddCount--;
                }
            }
            
            while (currentR < right) {
                currentR++;
                int val = nums[currentR];
                if (frequencies[val] == 0) {
                    distinctCount++;
                }
                frequencies[val]++;
                if (frequencies[val] % 2 != 0) {
                    oddCount++;
                } else {
                    oddCount--;
                }
            }
            
            while (currentL < left) {
                int val = nums[currentL];
                if (frequencies[val] % 2 != 0) {
                    oddCount--;
                } else {
                    oddCount++;
                }
                frequencies[val]--;
                if (frequencies[val] == 0) {
                    distinctCount--;
                }
                currentL++;
            }
            
            while (currentR > right) {
                int val = nums[currentR];
                if (frequencies[val] % 2 != 0) {
                    oddCount--;
                } else {
                    oddCount++;
                }
                frequencies[val]--;
                if (frequencies[val] == 0) {
                    distinctCount--;
                }
                currentR--;
            }

            ans[originalIndex] = (distinctCount == k && oddCount == 0);
        }

        return ans;
    }
}