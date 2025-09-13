# Leetcode 2512: Reward Top K Students
# https://leetcode.com/problems/reward-top-k-students/
# Solved on 13th of September, 2025
class Solution:
    def topStudents(self, positive_feedback: list[str], negative_feedback: list[str], report: list[str], student_id: list[int], k: int) -> list[int]:
        """
        Calculates the top k students based on their feedback scores.

        :param positive_feedback: A list of strings representing positive feedback words.
        :param negative_feedback: A list of strings representing negative feedback words.
        :param report: A list of strings, where each string is a student's report.
        :param student_id: A list of integers, where each integer is a student's ID.
        :param k: An integer representing the number of top students to return.
        :return: A list of integers representing the IDs of the top k students.
        """
        # Use sets for membership checks
        pos = set(positive_feedback)
        neg = set(negative_feedback)

        # Compute score for each student
        scores = []
        for sid, rep in zip(student_id, report):
            sc = 0
            # Reports consist of lowercase words separated by single spaces
            for w in rep.split():
                if w in pos:
                    sc += 3
                elif w in neg:
                    sc -= 1

            scores.append((sid, sc))

        # Sort by score descending, then by student id ascending
        scores.sort(key=lambda x: (-x[1], x[0]))

        # Return top k student ids
        return [sid for sid, _ in scores[:k]]