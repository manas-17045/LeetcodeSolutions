// Leetcode 3955: Valid Binary Strings With Cost Limit
// https://leetcode.com/problems/valid-binary-strings-with-cost-limit/
// Solved on 24th of June, 2026
class Solution {
    /**
     * Generates valid binary strings using backtracking.
     * 
     * @param n The length of the binary string.
     * @param k The cost limit.
     * @return The list of valid binary strings.
     */
    public List<String> generateValidStrings(int n, int k) {
        List<String> result = new ArrayList<>();
        char[] current = new char[n];
        backtrack(0, 0, false, current, result, n, k);
        return result;
    }

    private void backtrack(int index, int cost, boolean wasOne, char[] current, List<String> result, int n, int k) {
        if (index == n) {
            result.add(new String(current));
            return;
        }

        current[index] = '0';
        backtrack(index + 1, cost, false, current, result, n, k);

        if (!wasOne && cost + index <= k) {
            current[index] = '1';
            backtrack(index + 1, cost + index, true, current, result, n, k);
        }
    }
}