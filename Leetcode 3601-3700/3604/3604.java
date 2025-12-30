// Leetcode 3604: Minimum Time to Reach Destination in Directed Graph
// https://leetcode.com/problems/minimum-time-to-reach-destination-in-directed-graph/
// Solved on 30th of December, 2025
class Solution {
    /**
     * Calculates the minimum time to reach the destination node (n-1) from node 0 in a directed graph.
     * @param n The number of nodes in the graph.
     * @param edges A 2D array representing the edges, where each edge[i] = [u, v, start_time, end_time].
     * @return The minimum time to reach the destination, or -1 if it's not reachable.
     */
    public int minTime(int n, int[][] edges) {
        List<int[]>[] graph = new ArrayList[n];
        for (int i = 0; i < n; i++) {
            graph[i] = new ArrayList<>();
        }
        for (int[] edge : edges) {
            graph[edge[0]].add(new int[]{edge[1], edge[2], edge[3]});
        }

        int[] minTimes = new int[n];
        Arrays.fill(minTimes, Integer.MAX_VALUE);
        minTimes[0] = 0;

        PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> Integer.compare(a[0], b[0]));
        pq.offer(new int[]{0, 0});

        while (!pq.isEmpty()) {
            int[] current = pq.poll();
            int currentTime = current[0];
            int currentNode = current[1];

            if (currentTime > minTimes[currentNode]) {
                continue;
            }
            if (currentNode == n - 1) {
                return currentTime;
            }

            for (int[] neighbor : graph[currentNode]) {
                int nextNode = neighbor[0];
                int start = neighbor[1];
                int end = neighbor[2];

                int departureTime = Math.max(currentTime, start);
                if (departureTime <= end) {
                    int arrivalTime = departureTime + 1;
                    if (arrivalTime < minTimes[nextNode]) {
                        minTimes[nextNode] = arrivalTime;
                        pq.offer(new int[]{arrivalTime, nextNode});
                    }
                }
            }
        }
        return -1;
    }
}