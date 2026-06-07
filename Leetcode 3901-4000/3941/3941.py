# Leetcode 3941:  Password Strength
# https://leetcode.com/problems/password-strength/
# Solved on 7th of June, 2026
class Solution:
    def passwordStrength(self, password: str) -> int:
        """
        Calculates the strength of a password based on the types of unique characters it contains.

        :param password: The input string representing the password to evaluate.
        :return: An integer representing the total calculated strength.
        """
        uniqueChars = set(password)
        totalStrength = 0

        for eachChar in uniqueChars:
            if 'a' <= eachChar <= 'z':
                totalStrength += 1
            elif 'A' <= eachChar <= 'Z':
                totalStrength += 2
            elif '0' <= eachChar <= '9':
                totalStrength += 3
            elif eachChar in "!@#$":
                totalStrength += 5

        return totalStrength