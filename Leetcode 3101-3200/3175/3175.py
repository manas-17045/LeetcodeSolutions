# Leetcode 3175: Find The First Player to win K Games in a Row
# https://leetcode.com/problems/find-the-first-player-to-win-k-games-in-a-row/
# Solved on 3rd of January, 2026
class Solution:
    def findWinningPlayer(self, skills: list[int], k: int) -> int:
        """
        Finds the first player to win k games in a row.

        Args:
            skills: A list of integers representing the skill levels of players.
            k: An integer representing the number of consecutive wins required.

        Returns:
            The index of the first player to win k games in a row.
        """

        currentWinner = 0
        currentStreak = 0

        for i in range(1, len(skills)):
            if skills[currentWinner] > skills[i]:
                currentStreak += 1
            else:
                currentWinner = i
                currentStreak = 1

            if currentStreak == k:
                return currentWinner

        return currentWinner