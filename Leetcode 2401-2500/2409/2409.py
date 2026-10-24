# Leetcode 2409: Count Days Spent Together
# https://leetcode.com/problems/count-days-spent-together/
# Solved on 24th of October, 2026
class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        """
        Calculate the total number of days Alice and Bob are in Rome together.

        Parameters:
            arriveAlice (str): Alice's arrival date in "MM-DD" format.
            leaveAlice (str): Alice's departure date in "MM-DD" format.
            arriveBob (str): Bob's arrival date in "MM-DD" format.
            leaveBob (str): Bob's departure date in "MM-DD" format.

        Returns:
            int: The number of days both Alice and Bob are in Rome concurrently.
        """
        def toDayOfYear(dateStr: str) -> int:
            daysPerMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
            monthIndex = int(dateStr[:2]) - 1
            dayOfMonth = int(dateStr[3:])
            return sum(daysPerMonth[:monthIndex]) + dayOfMonth

        overlapStart = max(arriveAlice, arriveBob)
        overlapEnd = min(leaveAlice, leaveBob)

        if overlapStart > overlapEnd:
            return 0

        return toDayOfYear(overlapEnd) - toDayOfYear(overlapStart) + 1