// Leetcode 2942: Minimum Score of a Path Between Two Cities
// https://leetcode.com/problems/minimum-score-of-a-path-between-two-cities/
// Solved on 2nd of November, 2025
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

class Solution {
    /**
     * Calculates the minimum score of a path between two cities (city 1 and city n).
     * The score of a path is the minimum edge weight in that path.
     * @param n The number of cities.
     * @param roads A 2D array where roads[i] = [ui, vi, distancei] indicates a bidirectional road between cities ui and vi with distance distancei.
     * @return The minimum possible score of a path between city 1 and city n.
     */
    public int minScore(int n, int[][] roads) {
        List<List<int[]>> graph = new ArrayList<>(n + 1);
        for (int i = 0; i <= n; i++) {
            graph.add(new ArrayList<>());
        }

        for (int[] road : roads) {
            graph.get(road[0]).add(new int[]{road[1], road[2]});
            graph.get(road[1]).add(new int[]{road[0], road[2]});
        }

        int minScore = Integer.MAX_VALUE;
        boolean[] visited = new boolean[n + 1];
        Queue<Integer> queue = new LinkedList<>();

        queue.add(1);
        visited[1] = true;

        while (!queue.isEmpty()) {
            int node = queue.poll();

            for (int[] edge : graph.get(node)) {
                int neighbor = edge[0];
                int distance = edge[1];

                minScore = Math.min(minScore, distance);

                if (!visited[neighbor]) {
                    visited[neighbor] = true;
                    queue.add(neighbor);
                }
            }
        }

        return minScore;
    }
}