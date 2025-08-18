# Leetcode 679: 24 Game
# https://leetcode.com/problems/24-game/
# Solved on 18th of August, 2025
class Solution:
    def judgePoint24(self, cards: list[int]) -> bool:
        """
        Determines if it's possible to obtain the number 24 from a given list of four numbers
        using addition, subtraction, multiplication, and division.

        Args:
            cards (list[int]): A list of four integers representing the numbers to use.

        Returns:
            bool: True if 24 can be obtained, False otherwise.
        """
        numbers = [float(num) for num in cards]
        epsilon = 1e-6

        def solve(currentNumbers: list[float]) -> bool:
            listSize = len(currentNumbers)
            if listSize == 1:
                return abs(currentNumbers[0] - 24) < epsilon

            for i in range(listSize):
                for j in range(i + 1, listSize):
                    numOne = currentNumbers[i]
                    numTwo = currentNumbers[j]

                    remainingNumbers = []
                    for k in range(listSize):
                        if k != i and k != j:
                            remainingNumbers.append(currentNumbers[k])

                    possibleResults = [
                        numOne + numTwo,
                        numOne * numTwo,
                        numOne - numTwo,
                        numTwo - numOne,
                    ]

                    if abs(numTwo) > epsilon:
                        possibleResults.append(numOne / numTwo)
                    if abs(numOne) > epsilon:
                        possibleResults.append(numTwo / numOne)

                    for result in possibleResults:
                        if solve(remainingNumbers + [result]):
                            return True

            return False

        return solve(numbers)