# Leetcode 2162: Minimum Cost to Set Cooking Time
# https://leetcode.com/problems/minimum-cost-to-set-cooking-time/
# Solved on 22nd of November, 2025
class Solution:
    def minCostSetTime(self, startAt: int, moveCost: int, pushCost: int, targetSeconds: int) -> int:
        """
        Calculates the minimum cost to set a cooking time on a digital timer.

        Args:
            startAt (int): The initial digit the cursor is pointing at.
            moveCost (int): The cost to move the cursor to a different digit.
            pushCost (int): The cost to push a digit button.
            targetSeconds (int): The total cooking time in seconds.

        Returns:
            int: The minimum cost to set the target cooking time.
        """
        minCost = float('inf')

        minutesMax = targetSeconds // 60
        secondsMax = targetSeconds % 60

        candidates = [(minutesMax, secondsMax), (minutesMax - 1, secondsMax + 60)]

        for minutes, seconds in candidates:
            if not (0 <= minutes <= 99 and 0 <= seconds <= 99):
                continue

            targetNum = minutes * 100 + seconds
            targetStr = str(targetNum)

            currentCost = 0
            currentPos = startAt

            for char in targetStr:
                digit = int(char)
                if digit != currentPos:
                    currentCost += moveCost
                    currentPos = digit
                currentCost += pushCost

            if currentCost < minCost:
                minCost = currentCost

        return int(minCost)