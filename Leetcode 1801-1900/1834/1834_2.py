# Leetcode 1834: Single-Threaded CPU
# https://leetcode.com/problems/single-threaded-cpu/
# Solved on 27th of May, 2025
import heapq


class Solution:
    def getOrder(self, tasks: list[list[int]]) -> list[int]:
        """
        Given a list of tasks, where each task is represented as [enqueueTime, processingTime],
        return the order in which the CPU will process the tasks.

        The CPU processes tasks in the following order:
        1. At any given time, the CPU can only process one task.
        2. Tasks are processed in the order of their enqueue time.
        3. If multiple tasks have the same enqueue time, they are processed in the order of their processing time (shortest first).
        4. If multiple tasks have the same enqueue time and processing time, they are processed in the order of their original index (smallest first).

        Args:
            tasks: A list of lists, where each inner list represents a task [enqueueTime, processingTime].

        Returns:
            A list of integers representing the order in which the tasks are processed (original indices).
        """


        # Augment with original indices and sort by enqueue time
        tasks = [(enq, proc, i) for i, (enq, proc) in enumerate(tasks)]
        tasks.sort(key=lambda x: x[0])

        result = []
        min_heap = []   # (processing_time, original index)
        time = 0
        i = 0
        n = len(tasks)

        # Process until we've schedules all tasks
        while i < n or min_heap:
            # If no tasks are available, fast-forward time
            if not min_heap and time < tasks[i][0]:
                time = tasks[i][0]

            # Push all tasks that have become available by current time
            while i < n and tasks[i][0] <= time:
                enq, proc, idx = tasks[i]
                heapq.heappush(min_heap, (proc, idx))
                i += 1

            # Pop the next task to process
            proc, idx = heapq.heappop(min_heap)
            time += proc
            result.append(idx)

        return result