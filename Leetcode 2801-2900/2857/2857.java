// Leetcpde 2857: Count Pairs of Points With Distanc k
// https://leetcode.com/problems/count-pairs-of-points-with-distance-k/
// Solved on 6th of January, 2026
import java.util.HashMap;
import java.util.List;
import java.util.Map;

class Solution {
    /**
     * Counts the number of pairs of points (p1, p2) such that the XOR sum of their coordinates equals k.
     * Specifically, (p1.x ^ p2.x) + (p1.y ^ p2.y) == k.
     * @param coordinates A list of lists, where each inner list represents a point [x, y].
     * @param k The target XOR sum distance.
     * @return The number of such pairs.
     */
    public int countPairs(List<List<Integer>> coordinates, int k) {
        int count = 0;
        Map<Long, Integer> map = new HashMap<>();
        for (List<Integer> coordinate : coordinates) {
            int x = coordinate.get(0);
            int y = coordinate.get(1);
            for (int i = 0; i <= k; i++) {
                int targetX = x ^ i;
                int targetY = y ^ (k - i);
                long targetKey = ((long) targetX << 32) | targetY;
                count += map.getOrDefault(targetKey, 0);
            }
            long key = ((long) x << 32) | y;
            map.put(key, map.getOrDefault(key, 0) + 1);
        }
        return count;
    }
}