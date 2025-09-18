# Leetcode 3408: Design Task Manager
# https://leetcode.com/problems/design-task-manager/
# Solved on 18th of September, 2025
import heapq


class TaskManager:

    def __init__(self, tasks: list[list[int]]):
        # map taskId -> (userId, priority)
        self.task_info = {}
        # max-heap simulated via min-heap with negatives:
        # entries are (-priority, -taskId, taskId)
        self.heap = []

        for userId, taskId, priority in tasks:
            self.task_info[taskId] = (userId, priority)
            heapq.heappush(self.heap, (-priority, -taskId, taskId))

    def add(self, userId: int, taskId: int, priority: int) -> None:
        self.task_info[taskId] = (userId, priority)
        heapq.heappush(self.heap, (-priority, -taskId, taskId))

    def edit(self, taskId: int, newPriority: int) -> None:
        userId, _ = self.task_info[taskId]
        self.task_info[taskId] = (userId, newPriority)
        heapq.heappush(self.heap, (-newPriority, -taskId, taskId))

    def rmv(self, taskId: int) -> None:
        # Lazy deletion: remove from map; heap entries become stale
        if taskId in self.task_info:
            del self.task_info[taskId]

    def execTop(self) -> int:
        # Pop stale entries until top is valid or heap empty
        while self.heap:
            neg_prio, neg_tid, tid = self.heap[0]
            prio = -neg_prio
            # Check current state in map
            info = self.task_info.get(tid)
            if info is None:
                # Task was removed or executed earlier -> stale entry
                heapq.heappop(self.heap)
                continue
            cur_user, cur_prio = info
            if cur_prio != prio:
                # Stale entry with old priority
                heapq.heappop(self.heap)
                continue
            # Valid top; remove it from system and return userId
            heapq.heappop(self.heap)
            del self.task_info[tid]
            return cur_user
        return -1