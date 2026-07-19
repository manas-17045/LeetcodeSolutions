// Leetcode 3977: Minimum Time to Reach Target With Limited Power
// https://leetcode.com/problems/minimum-time-to-reach-target-with-limited-power/
// Solved on 19th of July, 2026
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.PriorityQueue;

class Solution {
    /**
     * Finds the minimum time to reach the target node from the source node with limited power.
     * @param n The number of nodes.
     * @param edges The edges.
     * @param power The initial power.
     * @param cost The cost to travel to each node.
     * @param source The source node.
     * @param target The target node.
     * @return An array of two integers representing the minimum time and maximum power.
     */
    public long[] minTimeMaxPower(int n, int[][] edges, int power, int[] cost, int source, int target) {
        List<int[]>[] adjList = new ArrayList[n];
        for (int i = 0; i < n; i++) {
            adjList[i] = new ArrayList<>();
        }
        for (int[] edge : edges) {
            adjList[edge[0]].add(new int[]{edge[1], edge[2]});
        }

        int[] maxPower = new int[n];
        Arrays.fill(maxPower, -1);

        PriorityQueue<long[]> pq = new PriorityQueue<>((a, b) -> {
            if (a[0] != b[0]) {
                return Long.compare(a[0], b[0]);
            }
            return Long.compare(b[2], a[2]);
        });

        pq.offer(new long[]{0, source, power});

        while (!pq.isEmpty()) {
            long[] curr = pq.poll();
            long currTime = curr[0];
            int currNode = (int) curr[1];
            int currPower = (int) curr[2];

            if (currNode == target) {
                return new long[]{currTime, currPower};
            }

            if (currPower <= maxPower[currNode]) {
                continue;
            }
            maxPower[currNode] = currPower;

            if (currPower >= cost[currNode]) {
                int nextPower = currPower - cost[currNode];
                for (int[] neighbor : adjList[currNode]) {
                    int nextNode = neighbor[0];
                    long nextTime = currTime + neighbor[1];
                    pq.offer(new long[]{nextTime, nextNode, nextPower});
                }
            }
        }

        return new long[]{-1, -1};
    }
}