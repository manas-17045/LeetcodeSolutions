// Leetcode 3315: Construct the Minimum Bitwise Array II
// https://leetcode.com/problems/construct-the-minimum-bitwise-array-ii/
// Solved on 21st of January, 2026
class Solution {
    /**
     * Constructs an array where each element is the minimum possible value obtained by
     * flipping at most one bit of the corresponding element in the input array.
     * @param nums A list of integers.
     * @return A list of integers where each element is the minimum bitwise value.
     */
    public int[] minBitwiseArray(List<Integer> nums) {
        int n = nums.size();
        int[] result = new int[n];
        for (int i = 0; i < n; i++) {
            int num = nums.get(i);
            if (num == 2) {
                result[i] = -1;
            } else {
                int trailingOnes = 0;
                int temp = num;
                while ((temp & 1) == 1) {
                    trailingOnes++;
                    temp >>= 1;
                }
                result[i] = num - (1 << (trailingOnes - 1));
            }
        }
        return result;
    }
}