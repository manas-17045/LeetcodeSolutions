// Leetcode 3371: Identify the Largest Outlier in an Array
// https://leetcode.com/problems/identify-the-largest-outlier-in-an-array/
// Solved on 24th of November, 2025
class Solution {
    /**
     * Identifies the largest outlier in an array. An outlier is defined as a number `num`
     * such that the sum of the remaining numbers in the array can be split into two equal halves.
     * @param nums The input array of integers.
     * @return The largest outlier found, or Integer.MIN_VALUE if no such outlier exists.
     */
    public int getLargestOutlier(int[] nums) {
        int totalSum = 0;
        int[] frequency = new int[2001];

        for (int num : nums) {
            totalSum += num;
            frequency[num + 1000]++;
        }

        int largestOutlier = Integer.MIN_VALUE;

        for (int num : nums) {
            int remaining = totalSum - num;

            if (remaining % 2 == 0) {
                int target = remaining / 2;

                if (target >= -1000 && target <= 1000) {
                    int count = frequency[target + 1000];
                    if (target == num) {
                        if (count > 1) {
                            largestOutlier = Math.max(largestOutlier, num);
                        }
                    } else {
                        if (count > 0) {
                            largestOutlier = Math.max(largestOutlier, num);
                        }
                    }
                }
            }
        }

        return largestOutlier;
    }
}