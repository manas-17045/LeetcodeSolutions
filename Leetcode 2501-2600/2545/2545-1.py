# Leetcode 2545: Sort the Students by Their Kth Score
# https://leetcode.com/problems/sort-the-students-by-their-kth-score/
# Solved on 11th of October, 2025
class Solution:
    def sortTheStudents(self, score: list[list[int]], k: int) -> list[list[int]]:
        """
        Sorts the students based on their score in the kth subject in descending order.

        Args:
            score (list[list[int]]): A list of lists where each inner list represents a student's scores in different subjects.
            k (int): The index of the subject to sort by.
        Returns:
            list[list[int]]: The sorted list of student scores.
        """
        sortedScores = sorted(score, key=lambda studentRow: studentRow[k], reverse=True)
        return sortedScores