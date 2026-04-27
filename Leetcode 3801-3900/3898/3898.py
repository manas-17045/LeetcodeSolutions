# Leetcode 3898: Find the Degree of Each Vertex
# https://leetcode.com/problems/find-the-degree-of-each-vertex/
# Solved on 26th of April, 2026
class Solution:
    def findDegrees(self, matrix: list[list[int]]) -> list[int]:
        """
        Calculates the degree of each vertex in a graph represented by an adjacency matrix.

        :param matrix: A 2D list of integers representing the adjacency matrix of the graph.
        :return: A list of integers where each element represents the degree of the corresponding vertex.
        """
        degreeList = []

        for vertexRow in matrix:
            degreeList.append(sum(vertexRow))

        return degreeList