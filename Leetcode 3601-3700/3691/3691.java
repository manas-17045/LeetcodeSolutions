// Leetcode 3691: Maximum Total Subarray Value II
// https://leetcode.com/problems/maximum-total-subarray-value-ii/
// Solved on 4th of November, 2025
import java.util.PriorityQueue;

class Solution {
    /**
     * Calculates the maximum total value of k non-overlapping subarrays, where the value of a subarray is its maximum element minus its minimum element.
     * @param nums The input array of integers.
     * @param k The number of non-overlapping subarrays to select.
     * @return The maximum total value.
     */
    public long maxTotalValue(int[] nums, int k) {
        int n = nums.length;
        int logN = 32 - Integer.numberOfLeadingZeros(n);
        int[][] minTable = new int[logN][n];
        int[][] maxTable = new int[logN][n];

        for (int i = 0; i < n; i++) {
            minTable[0][i] = nums[i];
            maxTable[0][i] = nums[i];
        }

        for (int j = 1; j < logN; j++) {
            int len = 1 << (j - 1);
            for (int i = 0; i + (1 << j) <= n; i++) {
                minTable[j][i] = Math.min(minTable[j - 1][i], minTable[j - 1][i + len]);
                maxTable[j][i] = Math.max(maxTable[j - 1][i], maxTable[j - 1][i + len]);
            }
        }

        PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> Integer.compare(b[0], a[0]));

        for (int i = 0; i < n; i++) {
            int len = n - i;
            int j = 31 - Integer.numberOfLeadingZeros(len);
            int min = Math.min(minTable[j][i], minTable[j][n - (1 << j)]);
            int max = Math.max(maxTable[j][i], maxTable[j][n - (1 << j)]);
            pq.offer(new int[]{max - min, i, n - 1});
        }

        long totalValue = 0;
        for (int i = 0; i < k; i++) {
            if (pq.isEmpty()) {
                break;
            }
            int[] top = pq.poll();
            totalValue += top[0];
            int l = top[1];
            int r = top[2];

            if (l < r) {
                int nextR = r - 1;
                int len = nextR - l + 1;
                int j = 31 - Integer.numberOfLeadingZeros(len);
                int min = Math.min(minTable[j][l], minTable[j][nextR - (1 << j) + 1]);
                int max = Math.max(maxTable[j][l], maxTable[j][nextR - (1 << j) + 1]);
                pq.offer(new int[]{max - min, l, nextR});
            }
        }

        return totalValue;
    }
}