# Leetcode 1904: The Number of Full Rounds You Have Played
# https://leetcode.com/problems/the-number-of-full-rounds-you-have-played/
# Solved on 14th of November, 2025
class Solution:
    def numberOfRounds(self, loginTime: str, logoutTime: str) -> int:
        """
        Calculates the number of full 15-minute rounds played between a login and logout time.

        Args:
            loginTime (str): The login time in "HH:MM" format.
            logoutTime (str): The logout time in "HH:MM" format.
        Returns:
            int: The number of full 15-minute rounds played.
        """
        loginH = int(loginTime[0:2])
        loginM = int(loginTime[3:5])
        loginMinutes = loginH * 60 + loginM

        logoutH = int(logoutTime[0:2])
        logoutM = int(logoutTime[3:5])
        logoutMinutes = logoutH * 60 + logoutM

        if loginMinutes > logoutMinutes:
            logoutMinutes += 1440

        startRoundTime = (loginMinutes + 14) // 15
        endRoundTime = logoutMinutes // 15

        return max(0, endRoundTime - startRoundTime)