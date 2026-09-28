// Leetcode 4036: Lexicographically Largest String After Pair Transformations
// https://leetcode.com/problems/lexicographically-largest-string-after-pair-transformations/
// Solved on 28th of September, 2026
class Solution {
    /**
     * Computes the lexicographically largest string that can be formed for each
     * count of initial characters by repeatedly merging adjacent identical letters.
     *
     * @param nums an array of integers representing the initial counts of character 'a'
     * @return an array of strings containing the lexicographically largest string for each count
     */
    public String[] largestString(int[] nums) {
        int n = nums.length;
        String[] result = new String[n];
        int zValue = 1 << 25;

        for (int i = 0; i < n; i++) {
            StringBuilder builder = new StringBuilder();
            int current = nums[i];

            while (current >= zValue) {
                builder.append('z');
                current -= zValue;
            }

            for (int bit = 24; bit >= 0; bit--) {
                if ((current & (1 << bit)) != 0) {
                    builder.append((char) ('a' + bit));
                }
            }

            result[i] = builder.toString();
        }

        return result;
    }
}