// Leetcode 3878: Count Good Subarrays
// https://leetcode.com/problems/count-good-subarrays/
// Solved on 29th of March, 2026
import java.util.HashMap;

class Solution {
    /**
     * Counts the number of good subarrays in the given integer array.
     * 
     * @param nums An array of integers.
     * @return The total number of subarrays that satisfy the "good" criteria.
     */
    public long countGoodSubarrays(int[] nums) {
        int n = nums.length;
        int[] leftViolator = new int[n];
        int[] rightViolator = new int[n];
        int[] lastPos = new int[30];
        
        for (int i = 0; i < 30; i++) {
            lastPos[i] = -1;
        }
        
        HashMap<Integer, Integer> lastSeen = new HashMap<>();
        
        for (int i = 0; i < n; i++) {
            int val = nums[i];
            int maxLeft = -1;
            
            for (int b = 0; b < 30; b++) {
                if ((val & (1 << b)) == 0) {
                    if (lastPos[b] > maxLeft) {
                        maxLeft = lastPos[b];
                    }
                } else {
                    lastPos[b] = i;
                }
            }
            
            if (lastSeen.containsKey(val)) {
                int prev = lastSeen.get(val);
                if (prev > maxLeft) {
                    maxLeft = prev;
                }
            }
            
            leftViolator[i] = maxLeft;
            lastSeen.put(val, i);
        }
        
        int[] nextPos = new int[30];
        for (int i = 0; i < 30; i++) {
            nextPos[i] = n;
        }
        
        for (int i = n - 1; i >= 0; i--) {
            int val = nums[i];
            int minRight = n;
            
            for (int b = 0; b < 30; b++) {
                if ((val & (1 << b)) == 0) {
                    if (nextPos[b] < minRight) {
                        minRight = nextPos[b];
                    }
                } else {
                    nextPos[b] = i;
                }
            }
            
            rightViolator[i] = minRight;
        }
        
        long ans = 0;
        for (int i = 0; i < n; i++) {
            long leftCount = i - leftViolator[i];
            long rightCount = rightViolator[i] - i;
            ans += leftCount * rightCount;
        }
        
        return ans;
    }
}