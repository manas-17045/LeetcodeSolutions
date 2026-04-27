// Leetcode 1391: Check if There is a Valid Path in a Grid
// https://leetcode.com/problems/check-if-there-is-a-valid-path-in-a-grid/
// Solved on 27th of April, 2026
class Solution {
    /**
     * Determines if there is a valid path from the top-left cell (0,0) to the bottom-right cell (m-1, n-1).
     * 
     * @param grid A 2D integer array representing the types of pipes in each cell.
     * @return true if a valid path exists, false otherwise.
     */
    public boolean hasValidPath(int[][] grid) {
        int numRows = grid.length;
        int numCols = grid[0].length;
        boolean[][] visitedCells = new boolean[numRows][numCols];
        int[][][] pipeDirections = {
            {},
            {{0, -1}, {0, 1}},
            {{-1, 0}, {1, 0}},
            {{0, -1}, {1, 0}},
            {{0, 1}, {1, 0}},
            {{0, -1}, {-1, 0}},
            {{0, 1}, {-1, 0}}
        };
        int[] bfsQueue = new int[numRows * numCols * 2];
        int queueHead = 0;
        int queueTail = 0;
        
        bfsQueue[queueTail++] = 0;
        bfsQueue[queueTail++] = 0;
        visitedCells[0][0] = true;
        
        while (queueHead < queueTail) {
            int currentRow = bfsQueue[queueHead++];
            int currentCol = bfsQueue[queueHead++];
            
            if (currentRow == numRows - 1 && currentCol == numCols - 1) {
                return true;
            }
            
            int currentPipe = grid[currentRow][currentCol];
            
            for (int[] direction : pipeDirections[currentPipe]) {
                int nextRow = currentRow + direction[0];
                int nextCol = currentCol + direction[1];
                
                if (nextRow >= 0 && nextRow < numRows && nextCol >= 0 && nextCol < numCols && !visitedCells[nextRow][nextCol]) {
                    int nextPipe = grid[nextRow][nextCol];
                    boolean hasConnection = false;
                    
                    for (int[] reverseDirection : pipeDirections[nextPipe]) {
                        if (reverseDirection[0] == -direction[0] && reverseDirection[1] == -direction[1]) {
                            hasConnection = true;
                            break;
                        }
                    }
                    
                    if (hasConnection) {
                        visitedCells[nextRow][nextCol] = true;
                        bfsQueue[queueTail++] = nextRow;
                        bfsQueue[queueTail++] = nextCol;
                    }
                }
            }
        }
        
        return false;
    }
}