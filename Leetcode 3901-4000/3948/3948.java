// Leetcode 3948: Lexicographicallt Maximum MEX Array
// https://leetcode.com/problems/lexicographically-maximum-mex-array/
// Solved on 14th of June, 2026
class Solution {
    /**
     * Finds the lexicographically maximum MEX array by greedily partitioning the input.
     * @param nums The input array of integers.
     * @return The lexicographically largest array of MEX values.
     */
    public int[] maximumMEX(int[] nums) {
        int n = nums.length;
        int[] freq = new int[n + 2];
        for (int i = 0; i < n; i++) {
            if (nums[i] <= n) {
                freq[nums[i]]++;
            }
        }
        int mex = 0;
        while (freq[mex] > 0) {
            mex++;
        }
        int[] tempResult = new int[n];
        int resultSize = 0;
        boolean[] seen = new boolean[n + 2];
        int i = 0;
        while (i < n) {
            int targetMex = mex;
            tempResult[resultSize++] = targetMex;
            if (targetMex == 0) {
                int val = nums[i];
                if (val <= n) {
                    freq[val]--;
                    if (freq[val] == 0 && val < mex) {
                        mex = val;
                    }
                }
                i++;
            } else {
                int count = 0;
                while (i < n && count < targetMex) {
                    int val = nums[i];
                    if (val < targetMex && !seen[val]) {
                        seen[val] = true;
                        count++;
                    }
                    if (val <= n) {
                        freq[val]--;
                        if (freq[val] == 0 && val < mex) {
                            mex = val;
                        }
                    }
                    i++;
                }
                for (int j = 0; j < targetMex; j++) {
                    seen[j] = false;
                }
            }
        }
        int[] finalResult = new int[resultSize];
        for (int j = 0; j < resultSize; j++) {
            finalResult[j] = tempResult[j];
        }
        return finalResult;
    }
}