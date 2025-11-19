// Leetcode 3737: Count Subarrays With Majority Element I
// https://leetcode.com/problems/count-subarrays-with-majority-element-i/
// Solved on 19th of November, 2025
class Solution {
    /**
     * Counts the number of subarrays where the target element is the majority element.
     * @param nums The input array of integers.
     * @param target The element to check for majority.
     * @return The total count of subarrays where 'target' is the majority element.
     */
    public int countMajoritySubarrays(int[] nums, int target) {
        int n = nums.length;
        int ans = 0;
        
        for (int i = 0; i < n; i++) {
            int count = 0;
            for (int j = i; j < n; j++) {
                if (nums[j] == target) {
                    count++;
                }
                int length = j - i + 1;
                if (count > length / 2) {
                    ans++;
                }
            }
        }
        
        return ans;
    }
}