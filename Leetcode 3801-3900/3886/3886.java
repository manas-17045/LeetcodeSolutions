// Leetcode 3886: Sum of Sortable Integers
// https://leetcode.com/problems/sum-of-sortable-integers/
// Solved on 8th of April, 2026
class Solution {
    /**
     * Calculates the sum of all integers k such that the array nums can be sorted
     * by partitioning it into segments of length k and rotating each segment.
     * @param nums An array of integers.
     * @return The sum of all valid segment lengths k.
     */
    public int sortableIntegers(int[] nums) {
        int n = nums.length;
        int sum = 0;
        for (int i = 1; i * i <= n; i++) {
            if (n % i == 0) {
                if (isValid(nums, n, i)) {
                    sum += i;
                }
                if (i * i != n) {
                    int k = n / i;
                    if (isValid(nums, n, k)) {
                        sum += k;
                    }
                }
            }
        }
        return sum;
    }

    private boolean isValid(int[] nums, int n, int k) {
        int prevMax = 0;
        for (int i = 0; i < n; i += k) {
            int start = i;
            int end = i + k - 1;
            int drops = 0;
            int curMin = nums[start];
            int curMax = nums[start];
            for (int j = start; j < end; j++) {
                if (nums[j] > nums[j + 1]) {
                    drops++;
                }
                if (nums[j + 1] < curMin) {
                    curMin = nums[j + 1];
                }
                if (nums[j + 1] > curMax) {
                    curMax = nums[j + 1];
                }
            }
            if (drops > 1) {
                return false;
            }
            if (drops == 1 && nums[end] > nums[start]) {
                return false;
            }
            if (curMin < prevMax) {
                return false;
            }
            prevMax = curMax;
        }
        return true;
    }
}