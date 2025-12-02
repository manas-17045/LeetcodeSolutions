// Leetcode 3719: Longest Balanced Subarray I
// https://leetcode.com/problems/longest-balanced-subarray-i/
// Solved on 2nd of November, 2025
class Solution {
    /**
     * Given an array of integers `nums`, return the length of the longest balanced subarray.
     * A subarray is balanced if the count of even numbers equals the count of odd numbers.
     * @param nums The input array of integers.
     * @return The length of the longest balanced subarray.
     */
    public int longestBalanced(int[] nums) {
        int maxLen = 0;
        int n = nums.length;
        int[] seen = new int[100001];

        for (int i = 0; i < n; i++) {
            if (n - i <= maxLen) {
                break;
            }
            int evenCount = 0;
            int oddCount = 0;
            for (int j = i; j < n; j++) {
                int val = nums[j];
                if (seen[val] != i + 1) {
                    seen[val] = i + 1;
                    if (val % 2 == 0) {
                        evenCount++;
                    } else {
                        oddCount++;
                    }
                }
                if (evenCount == oddCount) {
                    maxLen = Math.max(maxLen, j - i + 1);
                }
            }
        }
        return maxLen;
    }
}