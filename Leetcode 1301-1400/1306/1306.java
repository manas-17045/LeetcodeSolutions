// Leetcode 1306: Jump Game III
// https://leetcode.com/problems/jump-game-iii/
// Solved on 17th of May, 2026
class Solution {
    /**
     * Determines if you can reach any index with value 0 starting from the given index.
     * 
     * @param arr   An array of non-negative integers.
     * @param start The starting index.
     * @return true if a 0 is reachable, false otherwise.
     */
    public boolean canReach(int[] arr, int start) {
        if (start < 0 || start >= arr.length || arr[start] < 0) {
            return false;
        }
        if (arr[start] == 0) {
            return true;
        }
        int jump = arr[start];
        arr[start] = -jump;
        return canReach(arr, start + jump) || canReach(arr, start - jump);
    }
}