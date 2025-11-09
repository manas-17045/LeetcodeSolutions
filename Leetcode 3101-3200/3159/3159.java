// Leetcode 3159: Find Occurrences of an Element in an Array
// https://leetcode.com/problems/find-occurrences-of-an-element-in-an-array/
// Solved on 9th of November, 2025
import java.util.HashMap;
import java.util.ArrayList;

class Solution {
    /**
     * Finds the k-th occurrence of a specific element `x` in the `nums` array for each query.
     *
     * @param nums An array of integers where occurrences are to be found.
     * @param queries An array of integers, where each `queries[i]` represents the k-th occurrence to find.
     * @param x The target element whose occurrences are being sought.
     * @return An array `result` where `result[i]` is the index of the `queries[i]`-th occurrence of `x`, or -1 if not found.
     */
    public int[] occurrencesOfElement(int[] nums, int[] queries, int x) {
        HashMap<Integer, ArrayList<Integer>> map = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            int v = nums[i];
            ArrayList<Integer> list = map.get(v);
            if (list == null) {
                list = new ArrayList<>();
                map.put(v, list);
            }
            list.add(i);
        }
        int[] result = new int[queries.length];
        ArrayList<Integer> xList = map.get(x);
        for (int i = 0; i < queries.length; i++) {
            int k = queries[i];
            if (xList == null || k <= 0 || k > xList.size()) {
                result[i] = -1;
            } else {
                result[i] = xList.get(k - 1);
            }
        }
        return result;
    }
}