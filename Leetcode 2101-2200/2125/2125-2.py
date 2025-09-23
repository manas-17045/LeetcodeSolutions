# Leetcode 2125: Number of Laser Beams in a Bank
# https://leetcode.com/problems/number-of-laser-beams-in-a-bank/
# Solved on 23rd of September, 2025
class Solution:
    def numberOfBeams(self, bank: list[str]) -> int:
        """
        Calculates the total number of laser beams between security devices in a bank.
        :param bank: A list of strings representing the bank's layout, where '1' denotes a security device and '0' an empty space.
        :return: The total number of laser beams.
        """
        prev_count = 0
        total_beams = 0

        for row in bank:
            cur = row.count('1')
            if cur:
                # If there was a previous non-empty row, every device in that row
                # connects to every device in this row.
                total_beams += prev_count * cur
                prev_count = cur

        return total_beams