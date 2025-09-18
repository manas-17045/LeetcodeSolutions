# Leetcode 3408: Design Task Manager
# https://leetcode.com/problems/design-task-manager/
# Solved on 18th of September, 2025
import heapq


class TaskManager:

    def __init__(self, tasks: list[list[int]]):
        self.tasks = {}
        self.maxHeap = []
        for userId, taskId, priority in tasks:
            self.tasks[taskId] = (priority, userId)
            heapq.heappush(self.maxHeap, (-priority, -taskId, userId))

    def add(self, userId: int, taskId: int, priority: int) -> None:
        self.tasks[taskId] = (priority, userId)
        heapq.heappush(self.maxHeap, (-priority, -taskId, userId))

    def edit(self, taskId: int, newPriority: int) -> None:
        if taskId in self.tasks:
            currentPriority, userId = self.tasks[taskId]
            self.tasks[taskId] = (newPriority, userId)
            heapq.heappush(self.maxHeap, (-newPriority, -taskId, userId))

    def rmv(self, taskId) -> None:
        if taskId in self.tasks:
            del self.tasks[taskId]

    def execTop(self) -> int:
        while self.maxHeap:
            negPriority, negTaskId, userId = self.maxHeap[0]

            actualPriority = -negPriority
            actualTaskId = -negTaskId

            if actualTaskId not in self.tasks or self.tasks[actualTaskId] != (actualPriority, userId):
                heapq.heappop(self.maxHeap)
                continue

            heapq.heappop(self.maxHeap)
            del self.tasks[actualTaskId]
            return userId

        return -1