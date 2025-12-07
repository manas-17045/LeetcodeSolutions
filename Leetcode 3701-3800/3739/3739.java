// Leetcode 3739: Count Subarrays With Majority Element II
// https://leetcode.com/problems/count-subarrays-with-majority-element-ii/
// Solved on 7th of December, 2025
class Solution {
    /**
     * Counts the number of subarrays where the `target` element is the majority element.
     * A Fenwick tree (BIT) is used to efficiently count prefix sums.
     *
     * @param nums The input array of integers.
     * @param target The element to check for majority.
     * @return The total count of subarrays where `target` is the majority element.
     */
    public long countMajoritySubarrays(int[] nums, int target) {
        int n = nums.length;
        int[] bit = new int[2 * n + 2];
        int offset = n + 1;
        long count = 0;
        int currentSum = 0;

        update(bit, offset, 1);

        for (int num : nums) {
            if (num == target) {
                currentSum++;
            } else {
                currentSum--;
            }
            count += query(bit, currentSum - 1 + offset);
            update(bit, currentSum + offset, 1);
        }

        return count;
    }

    private void update(int[] bit, int index, int val) {
        while (index < bit.length) {
            bit[index] += val;
            index += index & (-index);
        }
    }

    private int query(int[] bit, int index) {
        int sum = 0;
        while (index > 0) {
            sum += bit[index];
            index -= index & (-index);
        }
        return sum;
    }
}