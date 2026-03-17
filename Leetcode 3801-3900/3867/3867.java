// Leetcode 3867: Sum of GCD of Formed Pairs
// https://leetcode.com/problems/sum-of-gcd-of-formed-pairs/
// Solved on 17th of March, 2026
import java.util.Arrays;

class Solution {
    /**
     * Calculates the sum of GCD values of pairs formed from the modified input array.
     *
     * @param nums An array of integers to process.
     * @return The total sum of GCDs of the formed pairs.
     */
    public long gcdSum(int[] nums) {
        int currentMax = 0;
        for (int i = 0; i < nums.length; i++) {
            currentMax = Math.max(currentMax, nums[i]);
            nums[i] = computeGcd(nums[i], currentMax);
        }

        Arrays.sort(nums);

        long sum = 0;
        int left = 0;
        int right = nums.length - 1;

        while (left < right) {
            sum += computeGcd(nums[left], nums[right]);
            left++;
            right--;
        }

        return sum;
    }

    private int computeGcd(int a, int b) {
        while (b != 0) {
            int temp = b;
            b = a % b;
            a = temp;
        }
        return a;
    }
}