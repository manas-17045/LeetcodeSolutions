# Leetcode 1834: Single-Threaded CPU
# https://leetcode.com/problems/single-threaded-cpu/
# Solved on 27th of May, 2025
import heapq


class Solution:
    def getOrder(self, tasks: list[list[int]]) -> list[int]:
        """
        Given a list of tasks, where tasks[i] = [enqueueTimei, processingTimei],
        you should return the order in which the CPU will process the tasks.

        Tasks are processed based on the following rules:
        1. The CPU is idle if it does not have any available tasks.
        2. If the CPU is idle and there are available tasks, it will start processing the task
           with the shortest processing time. If there is a tie in processing time, it will
           choose the task with the smallest index.
        3. If the CPU is busy, it will finish the current task before starting a new one.
        4. When the CPU finishes a task, it will immediately start processing the next available
           task according to rules 1 and 2.

        Args:
            tasks: A list of lists, where each inner list is [enqueueTime, processingTime].

        Returns:
            A list of integers representing the original indices of the tasks in the order they are processed.
        """
        num_tasks = len(tasks)

        # Augment tasks with their original indices: (enqueueTime, processingTime, originalIndex)
        # This is important for sorting by enqueueTime while keeping track of original order
        # and for tie-breaking using the original index.
        indexed_tasks = []
        for i in range(num_tasks):
            # tasks[i][0] is enqueueTime, tasks[i][1] is processingTime
            indexed_tasks.append((tasks[i][0], tasks[i][1], i))

        # Sort tasks primarily by enqueueTime. If enqueueTimes are the same,
        # Python's default sort is stable. The exact order for ties here doesn't critically
        # affect correctness, as the heap will handle selection among simultaneously available tasks based on
        # processing time and index.
        indexed_tasks.sort()

        result_order = []   # This list will store the indices of tasks in the order they are processed.

        # Min-heap to store tasks that are available for processing.
        # Tasks are stored as (processingTime, originalIndex).
        # heapq will prioritize tasks with shorter processingTime.
        # If processingTimes are equal, it will then prioritize by smaller originalIndex.
        available_tasks_heap = []

        currentTime = 0     # Represents the CPU's current clock time.
        task_pointer = 0    # An index to iterate through `indexed_tasks`.

        # The main simulation loop. Continues untill all tasks have been scheduled.
        while len(result_order) < num_tasks:
            # Add newly available tasks to the heap.
            # Iterate through `indexed_tasks` (starting from `task_pointer  ) and add any task
            # whose enqueueTime is less than or equal to `current_time` to `available_tasks_heap`.
            while task_pointer < num_tasks and indexed_tasks[task_pointer][0] <= currentTime:
                # _enqueueTime is not used directly after destructuring, hence the underscore.
                _enqueueTime, processing_time, original_index = indexed_tasks[task_pointer]
                heapq.heappush(available_tasks_heap, (processing_time, original_index))
                task_pointer += 1   # Move to the next task in the sorted list

            # Process the next task or handle CPU idle state.
            if available_tasks_heap:
                # If there are tasks in the heap, the CPU is busy.
                # Select the task with the shortest processingTime (and smallest index in case of a tie).
                processing_time, original_index = heapq.heappop(available_tasks_heap)

                # Record the task as processed.
                result_order.append(original_index)

                # Advance `current_time` by the processing_time of the task ust completed.
                # The CPU can start a new task instantly.
                currentTime += processing_time
            elif task_pointer < num_tasks:
                # If the heap is empty, but there are still tasks in `indexed_tasks` that haven't been considered:
                # This means the CPU is idle because no tasks are currently available.
                # The CPU must wait until the next task arrives.
                # The next task to arrive is `indexed_tasks[task_pointer]`.
                # Its enqueueTime is `indexed_tasks[task_pointer][0]`.
                # So, fast-forward `current_time` to this enqueueTime.
                # Note: `indexed_tasks[task_pointer][0]` will be `> current_time` here,
                # otherwise this task would have been added to the heap in Phase 1.
                currentTime = indexed_tasks[task_pointer][0]
            else:
                # This `else` branch implies:
                #   1. `available_tasks_heap` is empty (no tasks ready to run).
                #   2. `task_pointer == num_tasks` (all tasks from `indexed_tasks` have been considered for enqueuing).
                # If `len(result_order) < num_tasks` is still true at this point, it implies an issue or an
                # unexpected state. However, under normal operation, this path should effectively only be taken
                # when all tasks are processed, and `len(result_order) == num_tasks`,
                # at which point the outer `while` loop condition becomes false and terminates naturally.
                # This `break` acts as a safeguard for any unexpected scenarios.
                break

        return result_order