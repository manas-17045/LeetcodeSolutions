// Leetcode 1591: Strange Printer II
// https://leetcode.com/problems/strange-printer-ii/
// Solved on 10th of December, 2025
import java.util.HashSet;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Set;

class Solution {
    /**
     * Determines if the given target grid can be printed.
     *
     * @param targetGrid The target grid representing the final printed image.
     * @return True if the grid can be printed, false otherwise.
     */
    public boolean isPrintable(int[][] targetGrid) {
        int m = targetGrid.length;
        int n = targetGrid[0].length;
        int maxColor = 60;
        
        int[] minRow = new int[maxColor + 1];
        int[] maxRow = new int[maxColor + 1];
        int[] minCol = new int[maxColor + 1];
        int[] maxCol = new int[maxColor + 1];
        
        for (int i = 0; i <= maxColor; i++) {
            minRow[i] = Integer.MAX_VALUE;
            maxRow[i] = Integer.MIN_VALUE;
            minCol[i] = Integer.MAX_VALUE;
            maxCol[i] = Integer.MIN_VALUE;
        }
        
        Set<Integer> existingColors = new HashSet<>();
        
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                int color = targetGrid[i][j];
                existingColors.add(color);
                minRow[color] = Math.min(minRow[color], i);
                maxRow[color] = Math.max(maxRow[color], i);
                minCol[color] = Math.min(minCol[color], j);
                maxCol[color] = Math.max(maxCol[color], j);
            }
        }
        
        boolean[][] graph = new boolean[maxColor + 1][maxColor + 1];
        int[] inDegree = new int[maxColor + 1];
        
        for (int color : existingColors) {
            for (int i = minRow[color]; i <= maxRow[color]; i++) {
                for (int j = minCol[color]; j <= maxCol[color]; j++) {
                    int neighbor = targetGrid[i][j];
                    if (neighbor != color) {
                        if (!graph[color][neighbor]) {
                            graph[color][neighbor] = true;
                            inDegree[neighbor]++;
                        }
                    }
                }
            }
        }
        
        Queue<Integer> queue = new LinkedList<>();
        for (int color : existingColors) {
            if (inDegree[color] == 0) {
                queue.add(color);
            }
        }
        
        int processedCount = 0;
        while (!queue.isEmpty()) {
            int current = queue.poll();
            processedCount++;
            
            for (int i = 1; i <= maxColor; i++) {
                if (graph[current][i]) {
                    inDegree[i]--;
                    if (inDegree[i] == 0) {
                        queue.add(i);
                    }
                }
            }
        }
        
        return processedCount == existingColors.size();
    }
}