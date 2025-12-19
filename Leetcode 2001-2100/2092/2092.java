// Leetcode 2092: Find All People With Secret
// https://leetcode.com/problems/find-all-people-with-secret/
// Solved on 19th of December, 2025
import java.util.*;

class Solution {
    /**
     * Finds all people who eventually learn the secret.
     *
     * @param n The total number of people.
     * @param meetings A 2D array where meetings[i] = [x, y, t] indicates a meeting between person x and person y at time t.
     * @param firstPerson The first person (other than person 0) who initially knows the secret.
     * @return A list of integers representing all people who eventually learn the secret.
     */
    public List<Integer> findAllPeople(int n, int[][] meetings, int firstPerson) {
        Arrays.sort(meetings, (a, b) -> Integer.compare(a[2], b[2]));

        boolean[] hasSecret = new boolean[n];
        hasSecret[0] = true;
        hasSecret[firstPerson] = true;

        int length = meetings.length;
        int i = 0;

        while (i < length) {
            int j = i;
            while (j < length && meetings[j][2] == meetings[i][2]) {
                j++;
            }

            Map<Integer, List<Integer>> graph = new HashMap<>();
            Set<Integer> activeNodes = new HashSet<>();

            for (int k = i; k < j; k++) {
                int u = meetings[k][0];
                int v = meetings[k][1];

                graph.computeIfAbsent(u, x -> new ArrayList<>()).add(v);
                graph.computeIfAbsent(v, x -> new ArrayList<>()).add(u);

                if (hasSecret[u]) {
                    activeNodes.add(u);
                }
                if (hasSecret[v]) {
                    activeNodes.add(v);
                }
            }

            Queue<Integer> queue = new LinkedList<>(activeNodes);

            while (!queue.isEmpty()) {
                int curr = queue.poll();
                
                if (!graph.containsKey(curr)) {
                    continue;
                }

                for (int neighbor : graph.get(curr)) {
                    if (!hasSecret[neighbor]) {
                        hasSecret[neighbor] = true;
                        queue.offer(neighbor);
                    }
                }
            }
            i = j;
        }

        List<Integer> result = new ArrayList<>();
        for (int k = 0; k < n; k++) {
            if (hasSecret[k]) {
                result.add(k);
            }
        }
        return result;
    }
}