# Leetcode 3680: Generate Schedule
# https://leetcode.com/problems/generate-schedule/
# Solved on 28th of December, 2025
import sys


class Solution:
    def generateSchedule(self, n: int) -> list[list[int]]:
        """
        Generates a schedule of matches for n teams such that no team plays consecutive home or away games.

        Args:
            n: The number of teams.
        Returns:
            A list of lists, where each inner list represents a match [home_team, away_team].
        """
        if n <= 3:
            return []

        sys.setrecursionlimit(5000)

        adj = [set(i for i in range(n) if i != j) for j in range(n)]
        schedule = []
        totalMatches = n * (n - 1)

        def solve(lastHome, lastAway):
            if len(schedule) == totalMatches:
                return True

            validHomes = []
            for i in range(n):
                if i != lastHome and i != lastAway and adj[i]:
                    validHomes.append(i)

            validHomes.sort(key=lambda x: len(adj[x]), reverse=True)

            for home in validHomes:
                validAways = []
                for j in adj[home]:
                    if j != lastHome and j != lastAway:
                        validAways.append(j)

                validAways.sort(key=lambda x: len(adj[x]), reverse=True)

                for away in validAways:
                    adj[home].remove(away)
                    schedule.append([home, away])

                    if solve(home, away):
                        return True

                    schedule.pop()
                    adj[home].add(away)

            return False

        return schedule if solve(-1, -1) else []