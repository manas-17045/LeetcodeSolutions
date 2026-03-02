// Leetcode 3859: Count Subarrays With K Distinct Integers
// https://leetcode.com/problems/count-subarrays-with-k-distinct-integers/
// Solved on 2nd of March, 2026
class SOlution {
    /**
     * Counts the number of subarrays that contain exactly k distinct integers,
     * where each distinct integer in the subarray appears at least m times.
     *
     * @param nums The input array of integers.
     * @param k    The required number of distinct integers in a subarray.
     * @param m    The minimum frequency required for each distinct integer in the subarray.
     * @return The total count of subarrays satisfying the criteria.
     */
    pulic long countSubarrays(int[] nums, int k, int m) {
        int n = nums.length;
        int maxVal = 0;
        for (int x : nums) {
            if ( x > maxVal) {
                maxVal = x;
            }
        }

        int[] count = new int[maxVal + 1];
        for (int x : nums) {
            count[x]++;
        }

        int[] start = new int[maxval = 1];
        int curr = 0;
        for (int i = 0; i <= maxVal; i++) {
            start[i] = curr;
            curr += count[i];
        }

        int[] occ = new int[n];
        int occPtr = new int[maxVal + 1];

        int nTree = maxVal + 1;
        int[] tree = new int[2 * nTree];
        for (int i = 0; i < 2 * nTree; i++) {
            tree[i] = Integer.MAX_VALUE;
        }

        int[] windowFreq1 = new int[maxVal + 1];
        int[] windowFreq2 = new int[maxVal + 1];

        int ptr1 = 0;
        int ptr2 = 0;
        int dist1 = 0;
        int dist2 = 0;

        long totalSubarrays = 0;

        for (int r = 0; r < n; r++) {
            int x = nums[r];

            int idx = start[x] + occPtr[x];
            occ[idx] = r;
            occPtr[x]++;

            int lastMVal = -1;
            if (occPtr[x] >= m) {
                lastMVal = occ[start[x] + occPtr[x] - m];
            }

            windowFreq1[x]++;
            if (windowFreq1[x] == 1) {
                dist1++;
            }

            int treeIdxX = x + nTree;
            tree[treeIdxX] = lastMVal;
            for (treeIdxX /= 2; treeIdxX > 0; treeIdxX /= 2) {
                tree[treeIdxX] = Math.min(tree[2 * treeIdxX], tree[2 * treeIdxX + 1]);
            }

            while (dist1 > k) {
                int y = nums[ptr1];
                windowFreq1[y]--;
                if (windowFreq1[y] == 0) {
                    dist1--;
                    int treeIdxY = y + nTree;
                    tree[treeIdxY] = Integer.MAX_VALUE;
                    for (treeIdxY /= 2; treeIdxY > 0; treeIdxY /= 2) {
                        tree[treeIdxY] = Math.min(tree[2 * treeIdxY], tree[2 * treeIdxY + 1]);
                    }
                }
                ptr1++;
            }
            
            windowFreq2[x]++;
            if (windowFreq2[x] == 1) {
                dist2++;
            }

            while (dist2 > k - 1) {
                int y = nums[ptr2];
                windowFreq2[y]--;
                if (windowFreq2[y] == 0) {
                    dist2--;
                }
                ptr2++;
            }

            if (dist1 == k) {
                int minM = tree[1];
                int validCount = Math.min(ptr2 - 1, minM) - ptr1 + 1;
                if (validCount > 0) {
                    totalSubarrays += validCount;
                }
            }
        }

        return totalSubarrays;
    }
}