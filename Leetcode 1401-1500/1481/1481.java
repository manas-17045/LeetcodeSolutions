// Leetcode 1481: Least Number of Unique Integers after K Removals
// https://leetcode.com/problems/least-number-of-unique-integers-after-k-removals/
// Solved on 10th of November, 2025
import java.util.HashMap;

class Solution {
    /**
     * Finds the least number of unique integers after removing exactly k elements.
     * @param arr The input array of integers.
     * @param k The number of elements to remove.
     * @return The least number of unique integers remaining.
     */
    public int findLeastNumOfUniqueInts(int[] arr, int k) {
        int n = arr.length;
        if (n == 0) {
            return 0;
        }
        HashMap<Integer,Integer> freqMap = new HashMap<>();
        for (int v : arr) {
            freqMap.put(v, freqMap.getOrDefault(v, 0) + 1);
        }
        int unique = freqMap.size();
        if (k == 0) {
            return unique;
        }
        int[] bucket = new int[n + 1];
        for (int f : freqMap.values()) {
            bucket[f]++;
        }
        for (int freq = 1; freq <= n && k > 0; freq++) {
            if (bucket[freq] == 0) {
                continue;
            }
            int removeable = Math.min(bucket[freq], k / freq);
            k -= removeable * freq;
            unique -= removeable;
            if (removeable < bucket[freq]) {
                break;
            }
        }
        return unique;
    }
}