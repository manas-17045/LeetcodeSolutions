// Leetcode 3454: Separate Squares II
// https://leetcode.com/problems/separate-squares-ii/
// Solved on 15th of December, 2025
import java.util.Arrays;

class Solution {
    /**
     * Separates a set of squares into two equal-area halves by a horizontal line.
     * This method uses a sweep-line algorithm with a segment tree to calculate the total area
     * and then find the y-coordinate that divides the total area into two equal parts.
     * @param squares A 2D array where each inner array represents a square [x, y, side_length].
     * @return The y-coordinate of the horizontal line that separates the squares into two equal areas.
     */
    public double separateSquares(int[][] squares) {
        int n = squares.length;
        double[][] events = new double[2 * n][4];
        double[] xCoordsTemp = new double[2 * n];
        
        for (int i = 0; i < n; i++) {
            events[2 * i][0] = squares[i][1];
            events[2 * i][1] = 1;
            events[2 * i][2] = squares[i][0];
            events[2 * i][3] = squares[i][0] + squares[i][2];
            
            events[2 * i + 1][0] = squares[i][1] + squares[i][2];
            events[2 * i + 1][1] = -1;
            events[2 * i + 1][2] = squares[i][0];
            events[2 * i + 1][3] = squares[i][0] + squares[i][2];
            
            xCoordsTemp[2 * i] = squares[i][0];
            xCoordsTemp[2 * i + 1] = squares[i][0] + squares[i][2];
        }
        
        Arrays.sort(events, (a, b) -> Double.compare(a[0], b[0]));
        Arrays.sort(xCoordsTemp);
        
        int m = 0;
        for (int i = 0; i < 2 * n; i++) {
            if (i == 0 || xCoordsTemp[i] != xCoordsTemp[i - 1]) {
                m++;
            }
        }
        
        double[] xCoords = new double[m];
        int idx = 0;
        for (int i = 0; i < 2 * n; i++) {
            if (i == 0 || xCoordsTemp[i] != xCoordsTemp[i - 1]) {
                xCoords[idx++] = xCoordsTemp[i];
            }
        }
        
        int[] count = new int[4 * m];
        double[] len = new double[4 * m];
        
        double totalArea = 0;
        double prevY = events[0][0];
        
        double[] yCheckpoints = new double[2 * n];
        double[] areaCheckpoints = new double[2 * n];
        int cpIdx = 0;
        
        for (int i = 0; i < 2 * n; i++) {
            double y = events[i][0];
            double type = events[i][1];
            double x1 = events[i][2];
            double x2 = events[i][3];
            
            if (y > prevY) {
                double currentLen = len[0];
                totalArea += currentLen * (y - prevY);
                yCheckpoints[cpIdx] = y;
                areaCheckpoints[cpIdx] = totalArea;
                cpIdx++;
                prevY = y;
            }
            
            int lIdx = Arrays.binarySearch(xCoords, x1);
            int rIdx = Arrays.binarySearch(xCoords, x2);
            
            if (lIdx < rIdx) {
                update(0, 0, m - 2, lIdx, rIdx - 1, (int) type, count, len, xCoords);
            }
        }
        
        double target = totalArea / 2.0;
        double currentTotal = 0;
        prevY = events[0][0];
        
        for (int i = 0; i < cpIdx; i++) {
            if (areaCheckpoints[i] >= target) {
                double dy = yCheckpoints[i] - prevY;
                double da = areaCheckpoints[i] - currentTotal;
                return prevY + (target - currentTotal) * dy / da;
            }
            currentTotal = areaCheckpoints[i];
            prevY = yCheckpoints[i];
        }
        
        return prevY;
    }
    
    private void update(int node, int start, int end, int l, int r, int val, int[] count, double[] len, double[] xCoords) {
        if (l > end || r < start) return;
        
        if (l <= start && end <= r) {
            count[node] += val;
        } else {
            int mid = start + (end - start) / 2;
            update(2 * node + 1, start, mid, l, r, val, count, len, xCoords);
            update(2 * node + 2, mid + 1, end, l, r, val, count, len, xCoords);
        }
        
        if (count[node] > 0) {
            len[node] = xCoords[end + 1] - xCoords[start];
        } else if (start != end) {
            len[node] = len[2 * node + 1] + len[2 * node + 2];
        } else {
            len[node] = 0;
        }
    }
}