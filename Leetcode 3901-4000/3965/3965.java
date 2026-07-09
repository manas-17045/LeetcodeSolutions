// Leetcode 3965: Finish Time of Tasks I
// https://leetcode.com/problems/finish-time-of-tasks-i/    
// Solved on 9th of July, 2026
class Solution {
    /**
     * Calculates the minimum time required to finish all tasks.
     * 
     * @param n         The number of tasks, indexed from 0 to n-1.
     * @param edges     A 2D array where `edges[i] = [ai, bi]` indicates that task `ai` must be
     *                  completed before task `bi`.
     * @param baseTime  An array where `baseTime[i]` is the time required to complete task `i`.
     * @return The minimum time required to finish all tasks.
     */
    public long finishTime(int n, int[][] edges, int[] baseTime) {
        int[] parent = new int[n];
        int[] childCount = new int[n];
        long[] minChild = new long[n];
        long[] maxChild = new long[n];
        long[] finishTime = new long[n];
        
        for (int i = 0; i < n; i++) {
            minChild[i] = Long.MAX_VALUE;
            maxChild[i] = Long.MIN_VALUE;
            parent[i] = -1;
        }
        
        for (int i = 0; i < edges.length; i++) {
            int u = edges[i][0];
            int v = edges[i][1];
            parent[v] = u;
            childCount[u]++;
        }
        
        int[] queue = new int[n];
        int queueHead = 0;
        int queueTail = 0;
        
        for (int i = 0; i < n; i++) {
            if (childCount[i] == 0) {
                queue[queueTail++] = i;
            }
        }
        
        while (queueHead < queueTail) {
            int u = queue[queueHead++];
            if (minChild[u] == Long.MAX_VALUE) {
                finishTime[u] = baseTime[u];
            } else {
                finishTime[u] = maxChild[u] + (maxChild[u] - minChild[u]) + baseTime[u];
            }
            
            int p = parent[u];
            if (p != -1) {
                if (finishTime[u] < minChild[p]) {
                    minChild[p] = finishTime[u];
                }
                if (finishTime[u] > maxChild[p]) {
                    maxChild[p] = finishTime[u];
                }
                childCount[p]--;
                if (childCount[p] == 0) {
                    queue[queueTail++] = p;
                }
            }
        }
        
        return finishTime[0];
    }
}