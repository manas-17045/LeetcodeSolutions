# Leetcode 2933: High-Access Employees
# https://leetcode.com/problems/high-access-employees/
# Solved on 5th of November, 2025
from collections import defaultdict


class Solution:
    def findHighAccessEmployees(self, access_times: list[list[str]]) -> list[str]:
        """
        Finds employees who have high access, defined as accessing the system
        at least three times within a one-hour period.

        Args:
            access_times: A list of lists, where each inner list contains
                          [employee_name: str, access_time: str (HHMM format)].
        Returns:
            A list of names of employees who have high access.
        """

        employeeTimes = defaultdict(list)

        for name, timeStr in access_times:
            employeeTimes[name].append(int(timeStr))

        highAccessNames = set()

        for name, times in employeeTimes.items():
            times.sort()

            if len(times) < 3:
                continue

            for i in range(len(times) - 2):
                timeOne = times[i]
                timeThree = times[i + 2]

                if timeThree - timeOne < 100:
                    highAccessNames.add(name)
                    break

        return list(highAccessNames)