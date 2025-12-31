// Leetcode 3522: Calculate Score After Performing Instructions
// https://leetcode.com/problems/calculate-score-after-performing-instructions/
// Solved on 31st of December, 2025
class Solution {
    /**
     * Calculates the score based on a sequence of instructions and their corresponding values.
     * @param instructions An array of integers representing the instructions.
     * @param values An array of integers representing the values associated with each instruction.
     * @return The total calculated score.
     */
    public long calculateScore(int[] instructions, int[] values) {
        long score = 0;
        int currentIndex = 0;
        int n = instructions.length;
        boolean[] visited = new boolean[n];

        while (currentIndex >= 0 && currentIndex < n && !visited[currentIndex]) {
            visited[currentIndex] = true;

            if (instructions[currentIndex].equals("add")) {
                score += values[currentIndex];
                currentIndex++;
            } else {
                currentIndex += values[currentIndex];
            }
        }

        return score;
    }
}