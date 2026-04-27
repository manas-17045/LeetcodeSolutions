// Leetcode 3898: Find the Degree of Each Vertex
// https://leetcode.com/problems/find-the-degree-of-each-vertex/
// Solved on 26th of April, 2026
class Solution {
    /**
     * Calculates the degree of each vertex in a graph represented by an adjacency matrix.
     *
     * @param matrix A 2D integer array representing the adjacency matrix of the graph.
     * @return An integer array where each element at index i represents the degree of vertex i.
     */
    public int[] findDegrees(int[][] matrix) {
        int nodeCount = matrix.length;
        int[] degreeArray = new int[nodeCount];
        for (int rowIdx = 0; rowIdx < nodeCount; rowIdx++) {
            for (int colIdx = rowIdx + 1; colIdx < nodeCount; colIdx++) {
                if (matrix[rowIdx][colIdx] == 1) {
                    degreeArray[rowIdx]++;
                    degreeArray[colIdx]++;
                }
            }
        }
        return degreeArray;
    }
}