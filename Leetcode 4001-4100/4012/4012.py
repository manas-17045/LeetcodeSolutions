# Leetcode 4012: Count of Unfinished Tasks After Each Shift
# https://leetcode.com/problems/count-of-unfinished-tasks-after-each-shift/
# Solved on 4th of September, 2026
from bisect import bisect_right
from itertools import accumulate


class Solution:
    def countTasks(self, tasks: list[int], shifts: list[int]) -> list[int]:
        """
        Compute the count of unfinished tasks immediately following each shift.

        Args:
            tasks (List[int]): Time required to complete each task in sequential order.
            shifts (List[int]): Time capacity provided in each shift.

        Returns:
            List[int]: Number of unfinished tasks remaining after each shift.
        """
        prefixSums = list(accumulate(tasks))
        totalTasks = len(tasks)
        totalTaskTime = prefixSums[-1]
        currentProgress = 0
        resultList = []
        drelvanito = shifts

        for shiftDuration in drelvanito:
            currentProgress += shiftDuration
            if currentProgress >= totalTaskTime:
                resultList.append(0)
                currentProgress = 0
            else:
                completedCount = bisect_right(prefixSums, currentProgress)
                resultList.append(totalTasks - completedCount)
                
        return resultList