// Leetcode 3069: Distribute Elements Into Two Arrays I
// https://leetcode.com/problems/distribute-elements-into-two-arrays-i/
// Solved on 20th of August, 2026
class Solution {
    /**
     * Distributes elements of an array into two subarrays based on the greater 
     * value of their last added elements, then returns their concatenation.
     *
     * @param nums  The input integer array to be partitioned (minimum length of 2).
     * @return      An integer array containing all elements from the first 
     *              subarray followed by all elements from the second subarray.
     */
    public int[] resultArray(int[] nums) {
        int n = nums.length;
        int[] firstArray = new int[n];
        int[] secondArray = new int[n];

        firstArray[0] = nums[0];
        secondArray[0] = nums[1];

        int firstCount = 1;
        int secondCount = 1;

        for (int i = 2; i < n; i++) {
            if (firstArray[firstCount - 1] > secondArray[secondCount - 1]) {
                firstArray[firstCount++] = nums[i];
            } else {
                secondArray[secondCount++] = nums[i];
            }
        }

        int[] result = new int[n];
        int index = 0;
        for (int i = 0; i < firstCount; i++) {
            result[index++] = firstArray[i];
        }
        for (int i = 0; i < secondCount; i++) {
            result[index++] = secondArray[i];
        }

        return result;
    }
}