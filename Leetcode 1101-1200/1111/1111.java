// Leetcode 1111: Maximum Nesting Depth of Two Valid Parentheses Strings
// https://leetcode.com/problems/maximum-nesting-depth-of-two-valid-parentheses-strings/
// Solved on 30th of September, 2026
class Solution {
    /**
     * Splits a valid parentheses string into two disjoint subsequences such that
     * the maximum nesting depth of the two subsequences is minimized.
     *
     * @param seq the input valid parentheses string
     * @return an integer array indicating whether each character belongs to subsequence 0 or 1
     */
    public int[] maxDepthAfterSplit(String seq) {
        int length = seq.length();
        int[] answer = new int[length];
        int depth = 0;
        
        for (int i = 0; i < length; i++) {
            char currentChar = seq.charAt(i);
            if (currentChar == '(') {
                answer[i] = depth & 1;
                depth++;
            } else {
                depth--;
                answer[i] = depth & 1;
            }
        }

        return answer;
    }
}