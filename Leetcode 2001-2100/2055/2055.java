// Leetcode 2055: Plates Between Candles
// https://leetcode.com/problems/plates-between-candles/
// Solved on 7th of November, 2025
class Solution {
    /**
     * Calculates the number of plates between candles for given queries.
     * @param s The string representing plates and candles.
     * @param queries An array of queries, where each query is [start, end].
     * @return An array of integers, where each element is the number of plates between candles for the corresponding query.
     */
    public int[] platesBetweenCandles(String s, int[][] queries) {
        int n = s.length();
        char[] arr = s.toCharArray();
        int[] prefix = new int[n];
        int count = 0;
        for (int i = 0; i < n; i++) {
            if (arr[i] == '*') {
                count++;
            }
            prefix[i] = count;
        }
        int[] nearestLeft = new int[n];
        int last = -1;
        for (int i = 0; i < n; i++) {
            if (arr[i] == '|') {
                last = i;
            }
            nearestLeft[i] = last;
        }
        int[] nearestRight = new int[n];
        last = -1;
        for (int i = n - 1; i >= 0; i--) {
            if (arr[i] == '|') {
                last = i;
            }
            nearestRight[i] = last;
        }
        int m = queries.length;
        int[] result = new int[m];
        for (int i = 0; i < m; i++) {
            int left = queries[i][0];
            int right = queries[i][1];
            int leftCandle = nearestRight[left];
            int rightCandle = nearestLeft[right];
            if (leftCandle == -1 || rightCandle == -1 || leftCandle >= rightCandle) {
                result[i] = 0;
            } else {
                result[i] = prefix[rightCandle] - prefix[leftCandle];
            }
        }
        return result;
    }
}