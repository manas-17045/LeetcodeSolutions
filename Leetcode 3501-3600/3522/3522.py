# Leetcode 3522: Calculate Score After Performing Instructions
# https://leetcode.com/problems/calculate-score-after-performing-instructions/
# Solved on 31st of December, 2025
class Solution:
    def calculateScore(self, instructions: list[str], values: list[int]) -> int:
        """
        Calculates the final score after performing a series of instructions.

        :param instructions: A list of strings, where each string is either "add" or "jump".
        :param values: A list of integers, corresponding to the values used by each instruction.
        :return: The final calculated score.
        """
        currentIndex = 0
        currentScore = 0
        visitedIndices = set()
        n = len(instructions)

        while 0 <= currentIndex < n:
            if currentIndex in visitedIndices:
                break

            visitedIndices.add(currentIndex)

            command = instructions[currentIndex]
            val = values[currentIndex]

            if command == "add":
                currentScore += val
                currentIndex += 1
            else:
                currentIndex += val

        return currentScore