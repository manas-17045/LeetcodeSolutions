// Leetcode 3636: Threshold majority Queries
// https://leetcode.com/problems/threshold-majority-queries/
// Solved on 24th of November, 2025
import java.util.*;

class Solution {
    /**
     * Solves threshold majority queries on an array. For each query [left, right, threshold],
     * it finds the smallest number in the subarray nums[left...right] that appears at least 'threshold' times.
     * @param nums The input array of integers.
     * @param queries A 2D array of queries, where each query is [left, right, threshold].
     * @return An array of integers, where ans[i] is the answer to queries[i].
     */
    public int[] subarrayMajority(int[] nums, int[][] queries) {
        int n = nums.length;
        int m = queries.length;

        TreeSet<Integer> distinct = new TreeSet<>();
        for (int x : nums) {
            distinct.add(x);
        }

        Map<Integer, Integer> valToId = new HashMap<>();
        int[] idToVal = new int[distinct.size()];
        int k = 0;
        for (int x : distinct) {
            valToId.put(x, k);
            idToVal[k] = x;
            k++;
        }

        int[] a = new int[n];
        for (int i = 0; i < n; i++) {
            a[i] = valToId.get(nums[i]);
        }

        int blockSize = (int) Math.sqrt(n);
        Integer[] qIdx = new Integer[m];
        for (int i = 0; i < m; i++) {
            qIdx[i] = i;
        }

        Arrays.sort(qIdx, (i, j) -> {
            int b1 = queries[i][0] / blockSize;
            int b2 = queries[j][0] / blockSize;
            if (b1 != b2) {
                return b1 - b2;
            }
            return (b1 % 2 == 1) ? queries[j][1] - queries[i][1] : queries[i][1] - queries[j][1];
        });

        int[] cnt = new int[k];
        TreeSet<Integer>[] freqGroups = new TreeSet[n + 1];
        for (int i = 0; i <= n; i++) {
            freqGroups[i] = new TreeSet<>();
        }

        int maxFreq = 0;
        int l = 0, r = -1;
        int[] ans = new int[m];

        for (int i : qIdx) {
            int ql = queries[i][0];
            int qr = queries[i][1];
            int threshold = queries[i][2];

            while (l > ql) {
                l--;
                int val = a[l];
                int c = cnt[val];
                if (c > 0) {
                    freqGroups[c].remove(val);
                }
                c++;
                cnt[val] = c;
                freqGroups[c].add(val);
                if (c > maxFreq) {
                    maxFreq = c;
                }
            }
            while (r < qr) {
                r++;
                int val = a[r];
                int c = cnt[val];
                if (c > 0) {
                    freqGroups[c].remove(val);
                }
                c++;
                cnt[val] = c;
                freqGroups[c].add(val);
                if (c > maxFreq) {
                    maxFreq = c;
                }
            }
            while (l < ql) {
                int val = a[l];
                int c = cnt[val];
                freqGroups[c].remove(val);
                if (c == maxFreq && freqGroups[c].isEmpty()) {
                    maxFreq--;
                }
                c--;
                cnt[val] = c;
                if (c > 0) {
                    freqGroups[c].add(val);
                }
                l++;
            }
            while (r > qr) {
                int val = a[r];
                int c = cnt[val];
                freqGroups[c].remove(val);
                if (c == maxFreq && freqGroups[c].isEmpty()) {
                    maxFreq--;
                }
                c--;
                cnt[val] = c;
                if (c > 0) {
                    freqGroups[c].add(val);
                }
                r--;
            }

            if (maxFreq >= threshold) {
                ans[i] = idToVal[freqGroups[maxFreq].first()];
            } else {
                ans[i] = -1;
            }
        }

        return ans;
    }
}