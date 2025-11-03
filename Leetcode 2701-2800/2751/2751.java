// Leetcode 2751: Robot Collisions
// https://leetcode.com/problems/robot-collisions/
// Solved on 3rd of November, 2025
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Stack;

class Solution {
    /**
     * Simulates robot collisions and returns the healths of the robots that survive.
     * @param positions An array of integers representing the initial positions of the robots.
     * @param healths An array of integers representing the initial healths of the robots.
     * @param directions A string representing the initial directions of the robots ('L' for left, 'R' for right).
     * @return A list of integers representing the healths of the surviving robots, in their original order.
     */
    public List<Integer> survivedRobotsHealths(int[] positions, int[] healths, String directions) {
        int n = positions.length;
        Integer[] indices = new Integer[n];
        for (int i = 0; i < n; i++) {
            indices[i] = i;
        }

        Arrays.sort(indices, (a, b) -> Integer.compare(positions[a], positions[b]));

        Stack<Integer> stack = new Stack<>();

        for (int currentIndex : indices) {
            if (directions.charAt(currentIndex) == 'R') {
                stack.push(currentIndex);
            } else {
                while (!stack.isEmpty() && healths[currentIndex] > 0) {
                    int rightRobotIndex = stack.pop();

                    if (healths[currentIndex] > healths[rightRobotIndex]) {
                        healths[rightRobotIndex] = 0;
                        healths[currentIndex] -= 1;
                    } else if (healths[rightRobotIndex] > healths[currentIndex]) {
                        healths[currentIndex] = 0;
                        healths[rightRobotIndex] -= 1;
                        stack.push(rightRobotIndex);
                        break;
                    } else {
                        healths[rightRobotIndex] = 0;
                        healths[currentIndex] = 0;
                        break;
                    }
                }
            }
        }

        List<Integer> result = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            if (healths[i] > 0) {
                result.add(healths[i]);
            }
        }
        return result;
    }
}