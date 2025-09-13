# Leetcode 2512: Reward Top K Students
# https://leetcode.com/problems/reward-top-k-students/
# Solved on 13th of September, 2025
class Solution:
    def topStudents(self, positive_feedback: list[str], negative_feedback: list[str], report: list[str], student_id: list[int], k: int) -> list[int]:
        """
        Calculates the top k students based on their feedback reports.

        Args:
            positive_feedback: A list of strings representing positive feedback words.
            negative_feedback: A list of strings representing negative feedback words.
            report: A list of strings, where each string is a student's report.
            student_id: A list of integers, where each integer is the ID of a student.
            k: An integer representing the number of top students to return.

        Returns:
            A list of integers representing the IDs of the top k students, sorted by score
            (highest first) and then by student ID (lowest first).
        """
        positiveSet = set(positive_feedback)
        negativeSet = set(negative_feedback)

        studentData = []

        for i in range(len(report)):
            currentId = student_id[i]
            currentReport = report[i]
            currentScore = 0

            words = currentReport.split(' ')

            for word in words:
                if word in positiveSet:
                    currentScore += 3
                elif word in negativeSet:
                    currentScore -= 1

            studentData.append((-currentScore, currentId))

        studentData.sort()

        result = [studentInfo[1] for studentInfo in studentData[:k]]

        return result