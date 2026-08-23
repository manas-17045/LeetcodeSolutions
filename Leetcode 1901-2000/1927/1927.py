# Leetcode 1927: Sum Game
# https://leetcode.com/problems/sum-game/
# Solved on 23rd of August, 2026
class Solution:
    def sumGame(self, num: str) -> bool:
        """
        Determines if the first player has a winning strategy in the Sum Game.
        
        @param num: A string representing the initial state of the game.
        @return: True if the first player has a winning strategy, false otherwise.
        """
        halfLength = len(num) // 2
        leftSum = 0
        rightSum = 0
        leftQMarks =0
        rightQMarks = 0

        for charIndex in range(halfLength):
            if num[charIndex] == '?':
                leftQMarks += 1
            else:
                leftSum += int(num[charIndex])
                
            if num[charIndex + halfLength] == '?':
                rightQMarks += 1
            else:
                rightSum += int(num[charIndex + halfLength])

        return 2 * (leftSum - rightSum) != 9 * (rightQMarks - leftQMarks)