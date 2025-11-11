// Leetcode 2610: Convert an Array Into a 2D Array With Conditions
// https://leetcode.com/problems/convert-an-array-into-a-2d-array-with-conditions/
// Solved on 11th of November, 2025
import java.util.*;

class Solution {
    /**
     * Converts an array of integers into a 2D array with the following conditions:
     * 1. Each row contains distinct integers.
     * 2. The number of rows should be minimal.
     * @param nums The input array of integers.
     * @return A list of lists representing the 2D array.
     */
    public List<List<Integer>> findMatrix(int[] nums) {
        Map<Integer,Integer> freq = new HashMap<>();
        int max = 0;
        for (int v : nums) {
            int c = freq.getOrDefault(v, 0) + 1;
            freq.put(v, c);
            if (c > max) {
                max = c;
            }
        }
        List<List<Integer>> res = new ArrayList<>();
        for (int i = 0; i < max; i++) {
            res.add(new ArrayList<>());
        }
        for (Map.Entry<Integer,Integer> e : freq.entrySet()) {
            int val = e.getKey();
            int count = e.getValue();
            for (int i = 0; i < count; i++) {
                res.get(i).add(val);
            }
        }
        return res;
    }
}