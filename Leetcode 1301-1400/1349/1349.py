# Leetcode 1349: Maximum Students Taking Exam
# https://leetcode.com/problems/maximum-students-taking-exam/
# Solved on 13th of November, 2025
class Solution:
    def maxStudents(self, seats: list[list[str]]) -> int:
        """
        Calculates the maximum number of students that can be seated in a classroom
        such that no two students sit next to each other (horizontally or diagonally).

        :param seats: A list of lists of strings representing the classroom layout.
                      '.' denotes an empty seat, '#' denotes a broken seat.
        :return: The maximum number of students that can be seated.
        """
        rows = len(seats)
        cols = len(seats[0])
        dp = {0: 0}
        for row in seats:
            availableSeats = 0
            for i in range(cols):
                if row[i] == '.':
                    availableSeats |= (1 << i)
            newDp = {}
            for mask in range(1 << cols):
                if (mask & availableSeats) != mask:
                    continue
                if mask & (mask << 1):
                    continue
                studentCount = bin(mask).count('1')
                for prevMask in dp:
                    if (mask & (prevMask << 1)) or (mask & (prevMask >> 1)):
                        continue
                    score = dp[prevMask] + studentCount
                    if mask not in newDp or score > newDp[mask]:
                        newDp[mask] = score
            dp = newDp

        return max(dp.values())