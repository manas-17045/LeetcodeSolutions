// Leetcode 3074: Apple Redistribution into Boxes
// https://leetcode.com/problems/apple-redistribution-into-boxes/
// Solved on 24th of December, 2025
import java.util.Arrays;

class Solution {
    /**
     * Calculates the minimum number of boxes required to redistribute all apples.
     * @param apple An array representing the number of apples in each basket.
     * @param capacity An array representing the capacity of each box.
     * @return The minimum number of boxes needed.
     */
    public int minimumBoxes(int[] apple, int[] capacity) {
        int totalApples = 0;
        for (int a : apple) {
            totalApples += a;
        }

        Arrays.sort(capacity);

        int boxCount = 0;
        for (int i = capacity.length - 1; i >= 0; i--) {
            totalApples -= capacity[i];
            boxCount++;
            if (totalApples <= 0) {
                return boxCount;
            }
        }
        return boxCount;
    }
}