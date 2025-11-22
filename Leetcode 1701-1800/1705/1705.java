// Leetcode 1705: Maximum Number of Eaten Apples
// https://leetcode.com/problems/maximum-number-of-eaten-apples/
// Solved on 22nd of November, 2025
import java.util.PriorityQueue;

class Solution {
    /**
     * Calculates the maximum number of apples that can be eaten.
     * @param apples An array where `apples[i]` is the number of apples grown on day `i`.
     * @param days An array where `days[i]` is the number of days `apples[i]` will remain fresh.
     * @return The maximum number of apples that can be eaten.
     */
    public int eatenApples(int[] apples, int[] days) {
        PriorityQueue<int[]> queue = new java.util.PriorityQueue<>((a, b) -> a[0] - b[0]);
        int totalEaten = 0;
        int n = apples.length;

        for (int i = 0; i < n; i++) {
            if (apples[i] > 0) {
                queue.offer(new int[]{i + days[i], apples[i]});
            }
            while (!queue.isEmpty() && queue.peek()[0] <= i) {
                queue.poll();
            }
            if (!queue.isEmpty()) {
                int[] current = queue.peek();
                totalEaten++;
                current[1]--;
                if (current[1] == 0) {
                    queue.poll();
                }
            }
        }

        int currentDay = n;
        while (!queue.isEmpty()) {
            while (!queue.isEmpty() && queue.peek()[0] <= currentDay) {
                queue.poll();
            }
            if (queue.isEmpty()) {
                break;
            }
            int[] current = queue.poll();
            int daysAvailable = current[0] - currentDay;
            int canEat = Math.min(daysAvailable, current[1]);
            totalEaten += canEat;
            currentDay += canEat;
        }

        return totalEaten;
    }
}