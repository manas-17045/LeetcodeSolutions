# Leetcode 2545: Sort the Students by Their Kth Score
# https://leetcode.com/problems/sort-the-students-by-their-kth-score/
# Solved on 11th of October, 2025
class Solution:
    def sortTheStudents(self, score: list[list[int]], k: int) -> list[list[int]]:
        """
        Sorts the students based on their scores in a specific subject.

        Args:
            score (list[list[int]]): A 2D integer array where score[i][j] denotes the score of the ith student in the jth subject.
            k (int): The subject index (0-indexed) to sort the students by.

        Returns:
            list[list[int]]: The 2D array sorted in descending order based on the scores in the kth subject.
        """
        return sorted(score, key=lambda row: row[k], reverse=True)