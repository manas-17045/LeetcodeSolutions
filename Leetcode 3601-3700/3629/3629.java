// Leetcode 3629: Minimum Jumps to Reach End via Prime Teleportation
// https://leetcode.com/problems/minimum-jumps-to-reach-end-via-prime-teleportation/
// Solved on 29th of December, 2025
import java.util.ArrayList;
import java.util.Arrays;
import java.util.ArrayDeque;
import java.util.List;
import java.util.Queue;

class Solution {
    /**
     * Calculates the minimum number of jumps required to reach the end of an array using prime teleportation.
     * Jumps can be made to adjacent indices or to any index that shares a prime factor with the current index's value.
     * @param nums An array of integers where nums[i] represents the value at index i.
     * @return The minimum number of jumps to reach the last index (n-1) from the first index (0), or -1 if unreachable.
     */
    public int minJumps(int[] nums) {
        int n = nums.length;
        if (n <= 1) {
            return 0;
        }

        int maxVal = 0;
        for (int num : nums) {
            maxVal = Math.max(maxVal, num);
        }
        maxVal++;

        int[] spf = new int[maxVal];
        for (int i = 0; i < maxVal; i++) {
            spf[i] = i;
        }
        for (int i = 2; i * i < maxVal; i++) {
            if (spf[i] == i) {
                for (int j = i * i; j < maxVal; j += i) {
                    if (spf[j] == j) {
                        spf[j] = i;
                    }
                }
            }
        }

        List<Integer>[] primeGroups = new ArrayList[maxVal];
        for (int i = 0; i < n; i++) {
            int temp = nums[i];
            while (temp > 1) {
                int p = spf[temp];
                if (primeGroups[p] == null) {
                    primeGroups[p] = new ArrayList<>();
                }
                primeGroups[p].add(i);
                while (temp % p == 0) {
                    temp /= p;
                }
            }
        }

        int[] dist = new int[n];
        Arrays.fill(dist, -1);
        dist[0] = 0;

        Queue<Integer> queue = new ArrayDeque<>();
        queue.offer(0);

        boolean[] visitedPrimes = new boolean[maxVal];

        while (!queue.isEmpty()) {
            int u = queue.poll();
            if (u == n - 1) {
                return dist[u];
            }

            int[] adjacent = {u - 1, u + 1};
            for (int v : adjacent) {
                if (v >= 0 && v < n && dist[v] == -1) {
                    dist[v] = dist[u] + 1;
                    queue.offer(v);
                }
            }

            int val = nums[u];
            if (val > 1 && spf[val] == val) {
                if (!visitedPrimes[val]) {
                    visitedPrimes[val] = true;
                    if (primeGroups[val] != null) {
                        for (int v : primeGroups[val]) {
                            if (dist[v] == -1) {
                                dist[v] = dist[u] + 1;
                                queue.offer(v);
                            }
                        }
                    }
                }
            }
        }

        return -1;
    }
}