// Leetcode 1331: Rank Transform of an Array
// https://leetcode.com/problems/rank-transform-of-an-array/
// Solved on 12th of July, 2026
import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

class Solution {
    /**
     * Transforms an array by replacing each element with its rank.
     * 
     * @param arr The input array.
     * @return The transformed array with ranks.
     */
    public int[] arrayRankTransform(int[] arr) {
        int[] sortedArr = arr.clone();
        Arrays.sort(sortedArr);
        Map<Integer, Integer> rankMap = new HashMap<>();
        int currentRank = 1;
        for (int value : sortedArr) {
            if (!rankMap.containsKey(value)) {
                rankMap.put(value, currentRank);
                currentRank++;
            }
        }
        for (int i = 0; i < arr.length; i++) {
            arr[i] = rankMap.get(arr[i]);
        }
        return arr;
    }
}