# Leetcode 3965: Finish Time of Tasks I
# https://leetcode.com/problems/finish-time-of-tasks-i/
# Solved on 9th of July, 2026
class Solution:
    def finishTime(self, n: int, edges: list[list[int]], baseTime: list[int]) -> int:
        """
        Calculates the minimum time required to finish all tasks.
        
        :param n: The number of tasks, indexed from 0 to n-1.
        :param edges: A 2D array where `edges[i] = [ai, bi]` indicates that task `ai` must be
                      completed before task `bi`.
        :param baseTime: An array where `baseTime[i]` is the time required to complete task `i`.
        :return: The minimum time required to finish all tasks.
        """
        childCount = [0] * n
        parentArray = [-1] * n
        isLeaf = [True] * n

        for parent, child in edges:
            parentArray[child] = parent
            childCount[parent] += 1
            isLeaf[parent] = False

        minChildTime = [float('inf')] * n
        maxChildTime = [float('-inf')] * n
        finishTime = [0] * n

        taskQueue = [i for i in range(n) if childCount[i] == 0]

        for currentTask in taskQueue:
            if isLeaf[currentTask]:
                finishTime[currentTask] = baseTime[currentTask]
            else:
                finishTime[currentTask] = maxChildTime[currentTask] + (maxChildTime[currentTask] - minChildTime[currentTask]) + baseTime[currentTask]

            parentTask = parentArray[currentTask]
            if parentTask != -1:
                if finishTime[currentTask] < minChildTime[parentTask]:
                    minChildTime[parentTask] = finishTime[currentTask]
                if finishTime[currentTask] > maxChildTime[parentTask]:
                    maxChildTime[parentTask] = finishTime[currentTask]

                childCount[parentTask] -= 1
                if childCount[parentTask] == 0:
                    taskQueue.append(parentTask)

        return finishTime[0]