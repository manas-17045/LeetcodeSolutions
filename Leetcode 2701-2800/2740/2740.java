// Leetcode 2740: Find the Value of the Partition
// https://leetcode.com/problems/find-the-value-of-the-partition/
// Solved on 8th of January, 2026
import java.util.Arrays;

class Solution {
    /**
     * Finds the minimum possible value of the partition.
     * @param nums The input array of integers.
     * @return The minimum difference between the maximum of the first partition and the minimum of the second partition.
     */
    public int findValueOfPartition(int[] nums) {
        Arrays.sort(nums);
        int minPartitionValue = Integer.MAX_VALUE;
        for (int i = 0; i < nums.length - 1; i++) {
            int currentDifference = nums[i + 1] - nums[i];
            if (currentDifference < minPartitionValue) {
                minPartitionValue = currentDifference;
            }
        }
        return minPartitionValue;
    }
}