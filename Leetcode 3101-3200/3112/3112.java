// Leetcode 3112: Minimum Time to Visit Disappearing Nodes
// https://leetcode.com/problems/minimum-time-to-visit-disappearing-nodes/
// Solved on 4th of January, 2026
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.PriorityQueue;

class Solution {
    /**
     * Calculates the minimum time to visit each node, considering that nodes disappear at a certain time.
     * @param n The number of nodes in the graph.
     * @param edges A 2D array representing the edges, where each edge is [u, v, length].
     * @param disappear An array where disappear[i] is the time at which node i disappears.
     * @return An array `answer` where `answer[i]` is the minimum time to reach node `i`, or -1 if it's unreachable before disappearing.
     */
    public int[] minimumTime(int n, int[][] edges, int[]disappear) {
        List<List<int[]>> graph = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            graph.add(new ArrayList<>());
        }

        for (int[] edge : edges) {
            int u = edge[0];
            int v = edge[1];
            int length = edge[2];
            graph.get(u).add(new int[]{v, length});
            graph.get(v).add(new int[]{u, length});
        }

        int[] answer = new int[n];
        Arrays.fill(answer, -1);
        answer[0] = 0;

        PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> a[0] - b[0]);
        pq.offer(new int[]{0, 0});

        while (!pq.isEmpty()) {
            int[] current = pq.poll();
            int time = current[0];
            int node = current[1];

            if (answer[node] != -1 && time > answer[node]) {
                continue;
            }

            for (int[] neighbor : graph.get(node)) {
                int nextNode = neighbor[0];
                int length = neighbor[1];
                int newTime = time + length;

                if (newTime < disappear[nextNode]) {
                    if (answer[nextNode] == -1 || newTime < answer[nextNode]) {
                        answer[nextNode] = newTime;
                        pq.offer(new int[]{newTime, nextNode});
                    }
                }
            }
        }

        return answer;
    }
}