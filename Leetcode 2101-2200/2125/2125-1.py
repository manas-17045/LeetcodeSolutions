# Leetcode 2125: Number of Laser Beams in a Bank
# https://leetcode.com/problems/number-of-laser-beams-in-a-bank/
# Solved on 23rd of September, 2025
class Solution:
    def numberOfBeams(self, bank: list[str]) -> int:
        """
        Calculates the total number of laser beams between security devices in a bank.

        Args:
            bank: A list of strings representing the bank's layout, where '1' denotes a security device
                  and '0' denotes an empty space.
        Returns:
            The total number of laser beams.
        """
        totalBeams = 0
        previousDeviceCount = 0

        for row in bank:
            currentDeviceCount = row.count('1')

            if currentDeviceCount > 0:
                totalBeams += previousDeviceCount * currentDeviceCount
                previousDeviceCount = currentDeviceCount

        return totalBeams