// Leetcode 3960: Frequency Balance Subarray
// https://leetcode.com/problems/frequency-balance-subarray/
// Solved on 29th of June, 2026
import java.util.Arrays;
import java.util.HashMap;

class Solution {
    /**
     * Computes the length of the longest frequency-balanced subarray.
     * A frequency-balanced subarray is a subarray where the count of each
     * distinct element is equal to the square of some integer k, or the count
     * of one element is double the count of another element.
     * 
     * @param nums The input array of integers.
     * @return The length of the longest frequency-balanced subarray.
     */
    public int getlength(int[] nums) {
        int n = nums.length;
        HashMap<Integer, Integer> map = new HashMap<>();
        int id = 0;
        int[] compressed = new int[n];
        for (int i = 0; i < n; i++) {
            if (!map.containsKey(nums[i])) {
                map.put(nums[i], id++);
            }
            compressed[i] = map.get(nums[i]);
        }
        int[] counts = new int[id];
        int[] freqCounts = new int[n + 1];
        int[] activeFreqList = new int[n + 1];
        int[] freqIndex = new int[n + 1];
        int maxLength = 0;
        for (int i = 0; i < n; i++) {
            Arrays.fill(counts, 0);
            Arrays.fill(freqCounts, 0);
            Arrays.fill(freqIndex, -1);
            int activeFreqSize = 0;
            int distinctValues = 0;
            for (int j = i; j < n; j++) {
                int val = compressed[j];
                int oldFreq = counts[val];
                int newFreq = oldFreq + 1;
                counts[val] = newFreq;
                if (oldFreq == 0) {
                    distinctValues++;
                }
                if (oldFreq > 0) {
                    freqCounts[oldFreq]--;
                    if (freqCounts[oldFreq] == 0) {
                        int idx = freqIndex[oldFreq];
                        int lastF = activeFreqList[activeFreqSize - 1];
                        activeFreqList[idx] = lastF;
                        freqIndex[lastF] = idx;
                        freqIndex[oldFreq] = -1;
                        activeFreqSize--;
                    }
                }
                freqCounts[newFreq]++;
                if (freqCounts[newFreq] == 1) {
                    activeFreqList[activeFreqSize] = newFreq;
                    freqIndex[newFreq] = activeFreqSize;
                    activeFreqSize++;
                }
                if (distinctValues == 1) {
                    if (j - i + 1 > maxLength) {
                        maxLength = j - i + 1;
                    }
                } else if (activeFreqSize == 2) {
                    int f1 = activeFreqList[0];
                    int f2 = activeFreqList[1];
                    if (f1 > f2) {
                        int temp = f1;
                        f1 = f2;
                        f2 = temp;
                    }
                    if (f2 == 2 * f1) {
                        if (j - i + 1 > maxLength) {
                            maxLength = j - i + 1;
                        }
                    }
                }
            }
        }
        return maxLength;
    }
}