// Leetcode 3528: Unit Conversion I
// https://leetcode.com/problems/unit-conversion-i/
// Solved on 30th of December, 2025
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

class Solution {
    /**
     * Calculates the conversion factors from a base unit (unit 0) to all other units.
     * The conversion factors are calculated modulo 10^9 + 7.
     * @param conversions A 2D array where each element `[source, target, factor]` represents that `1 unit of source = factor units of target`.
     * @return An array `result` where `result[i]` is the conversion factor from unit 0 to unit `i`.
     */
    public int[] baseUnitConversions(int[][] conversions) {
        int n = conversions.length + 1;
        List<List<int[]>> graph = new ArrayList<>(n);
        for (int i = 0; i < n; i++) {
            graph.add(new ArrayList<>());
        }

        for (int[] conversion : conversions) {
            int source = conversion[0];
            int target = conversion[1];
            int factor = conversion[2];
            graph.get(source).add(new int[]{target, factor});
        }

        long[] values = new long[n];
        values[0] = 1;
        long mod = 1000000007L;

        Queue<Integer> queue = new LinkedList<>();
        queue.offer(0);

        while (!queue.isEmpty()) {
            int current = queue.poll();
            long currentValue = values[current];

            for (int[] edge : graph.get(current)) {
                int nextNode = edge[0];
                long factor = edge[1];
                values[nextNode] = (currentValue * factor) % mod;
                queue.offer(nextNode);
            }
        }

        int[] result = new int[n];
        for (int i = 0; i < n; i++) {
            result[i] = (int) values[i];
        }

        return result;
    }
}