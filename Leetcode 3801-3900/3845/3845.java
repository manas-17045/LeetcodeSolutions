// Leetcode 3845: Maximum Subarray XOR with Bounded Range
// https://leetcode.com/problems/maximum-subarray-xor-with-bounded-range/
// Solved on 20th of February, 2026
class Solution {
    /**
     * Calculates the maximum XOR sum of a subarray such that the difference between 
     * the maximum and minimum elements in that subarray is at most k.
     *
     * @param nums An array of integers.
     * @param k The maximum allowed difference between the max and min elements in a subarray.
     * @return The maximum XOR sum found among all valid subarrays.
     */
    public int maxXor(int[] nums, int k) {
        int n = nums.length;
        int[][] trie = new int[n * 16 + 5][2];
        int[] cnt = new int[n * 16 + 5];
        int idx = 0;
        
        int[] px = new int[n + 1];
        for (int i = 0; i < n; i++) {
            px[i + 1] = px[i] ^ nums[i];
        }
        
        int[] minQ = new int[n];
        int[] maxQ = new int[n];
        int minHead = 0;
        int minTail = 0;
        int maxHead = 0;
        int maxTail = 0;
        
        int l = 0;
        int ans = 0;
        
        for (int r = 0; r < n; r++) {
            while (maxTail > maxHead && nums[maxQ[maxTail - 1]] <= nums[r]) {
                maxTail--;
            }
            maxQ[maxTail++] = r;
            
            while (minTail > minHead && nums[minQ[minTail - 1]] >= nums[r]) {
                minTail--;
            }
            minQ[minTail++] = r;
            
            while (nums[maxQ[maxHead]] - nums[minQ[minHead]] > k) {
                int valToRemove = px[l];
                int node = 0;
                for (int i = 14; i >= 0; i--) {
                    int bit = (valToRemove >> i) & 1;
                    node = trie[node][bit];
                    cnt[node]--;
                }
                l++;
                if (maxHead < maxTail && maxQ[maxHead] < l) {
                    maxHead++;
                }
                if (minHead < minTail && minQ[minHead] < l) {
                    minHead++;
                }
            }
            
            int valToInsert = px[r];
            int currNode = 0;
            for (int i = 14; i >= 0; i--) {
                int bit = (valToInsert >> i) & 1;
                if (trie[currNode][bit] == 0) {
                    trie[currNode][bit] = ++idx;
                }
                currNode = trie[currNode][bit];
                cnt[currNode]++;
            }
            
            int valToQuery = px[r + 1];
            int queryNode = 0;
            int currentMax = 0;
            for (int i = 14; i >= 0; i--) {
                int bit = (valToQuery >> i) & 1;
                int opp = 1 - bit;
                if (trie[queryNode][opp] != 0 && cnt[trie[queryNode][opp]] > 0) {
                    currentMax |= (1 << i);
                    queryNode = trie[queryNode][opp];
                } else {
                    queryNode = trie[queryNode][bit];
                }
            }
            if (currentMax > ans) {
                ans = currentMax;
            }
        }
        return ans;
    }
}