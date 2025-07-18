# Leetcode 2019: The Score of Students Solving Math Expression
# https://leetcode.com/problems/the-score-of-students-solving-math-expressions/
# Solved on 18th of July, 2025
class Solution:
    def scoreOfStudents(self, s: str, answers: list[int]) -> int:
        """
        Calculates the total score of students based on their answers to a math expression.
        :param s: The math expression as a string.
        :param answers: A list of integers representing the students' answers.
        :return: The total score.
        """
        nums = [int(char) for char in s if char.isdigit()]
        ops = [char for char in s if not char.isdigit()]
        numCount = len(nums)

        correctAnswer = eval(s)

        memo = {}

        def getPossibleResults(i: int, j: int) -> set[int]:
            if (i, j) in memo:
                return memo[(i, j)]

            if i == j:
                return {nums[i]}

            currentPossibleResults = set()

            for k in range(i, j):
                leftResults = getPossibleResults(i, k)
                rightResults = getPossibleResults(k + 1, j)

                op = ops[k]

                for val1 in leftResults:
                    for val2 in rightResults:
                        result = 0
                        if op == '+':
                            result = val1 + val2
                        else:
                            result = val1 * val2

                        if result <= 1000:
                            currentPossibleResults.add(result)

            memo[(i, j)] = currentPossibleResults
            return currentPossibleResults

        allPossibleAnswers = getPossibleResults(0, (numCount - 1))

        totalScore = 0
        for ans in answers:
            if ans == correctAnswer:
                totalScore += 5
            elif ans in allPossibleAnswers:
                totalScore += 2

        return totalScore