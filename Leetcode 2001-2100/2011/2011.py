# Leetcode 2011: Final Value of Variable After Performing Operations
# https://leetcode.com/problems/final-value-of-variable-after-performing-operations/
# Solved on 20th of October, 2025
class Solution:
    def finalValueAfterOperations(self, operations: list[str]) -> int:

        finalValue = 0
        for currentOperation in operations:
            if currentOperation[1] == '+':
                finalValue += 1
            else:
                finalValue -= 1
        return finalValue