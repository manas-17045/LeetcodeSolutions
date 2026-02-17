# Leetcode 401: Binary Watch
# https://leetcode.com/problems/binary-watch/
# Solved on 17th of February, 2026
class Solution:
    def readBinaryWatch(self, turnedOn: int) -> list[str]:
        """
        Returns all possible times the binary watch could represent for a given number of LEDs turned on.

        :param turnedOn: The total number of LEDs that are currently on (0-10).
        :return: A list of strings representing valid times in "h:mm" format.
        """
        validTimes = []
        for hour in range(12):
            for minute in range(60):

                if (bin(hour).count('1') + bin(minute).count('1')) == turnedOn:
                    validTimes.append(f"{hour}:{minute:02d}")

        return validTimes