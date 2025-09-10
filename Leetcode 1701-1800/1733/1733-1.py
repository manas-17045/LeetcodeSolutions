# Leetcode 1733: Minimum Number of People to Teach
# https://leetcode.com/problems/minimum-number-of-people-to-teach/
# Solved on 10th of September, 2025
import collections


class Solution:
    def minimumTeachings(self, n: int, languages: list[list[int]], friendships: list[list[int]]) -> int:
        """
        Calculates the minimum number of people to teach a common language so that all specified friendships can communicate.

        Args:
            n (int): The total number of languages available (1 to n).
            languages (list[list[int]]): A list where each inner list represents the languages spoken by a user.
            friendships (list[list[int]]): A list of pairs [u, v] indicating a friendship between user u and user v.

        Returns:
            int: The minimum number of people that need to be taught a new language.
        """
        languageSets = [set(userLanguages) for userLanguages in languages]

        unconnectedUsers = set()
        for u,v in friendships:
            userU = u - 1
            userV = v - 1

            if not languageSets[userU].intersection(languageSets[userV]):
                unconnectedUsers.add(userU)
                unconnectedUsers.add(userV)

        if not unconnectedUsers:
            return 0

        langCounts = collections.defaultdict(int)
        for userIndex in unconnectedUsers:
            for lang in languageSets[userIndex]:
                langCounts[lang] += 1

        maxKnownCount = 0
        if langCounts:
            maxKnownCount = max(langCounts.values())

        result = len(unconnectedUsers) - maxKnownCount
        return result