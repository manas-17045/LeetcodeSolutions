# Leetcode 2589: Minimum Time to Complete All Tasks
# https://leetcode.com/problems/minimum-time-to-complete-all-tasks/
# Solved on 27th of May, 2025

class Solution:
    def findMinimumTime(self, tasks: list[list[int]]) -> int:
        # Sort tasks by their end times.
        """
        Given a list of tasks, where each task is represented as [start, end, duration],
        find the minimum total time the computer needs to be turned on to complete all tasks.
        A task [start, end, duration] requires the computer to be on for 'duration' seconds
        within the time interval [start, end].

        The approach is to sort the tasks by their end times and greedily schedule the
        necessary computer on-time for each task, prioritizing later available times
        within the task's interval.

        Args:
            tasks: A list of tasks, where each task is [start_i, end_i, duration_i].
        Returns:
            The minimum total time the computer needs to be on.
        """
        # Tasks[i] = [start_i, end_i, duration_i]
        tasks.sort(key=lambda x: x[1])

        # Max possible end time is 2000 according to constraints.
        # Time slots are 1-indexed.
        # Time_on[t] is true if computer is on at time t.
        # We use indices 1 to 2000. Array size 2001 for convenience (0-th index unused).
        time_on = [False] * 2001

        # total_computer_on_time will store the count of 'True' values in time_on,
        # which represents the total number of distinct time units the computer is active.
        total_computer_on_time = 0

        for task_details in tasks:
            start_i, end_i, duration_i = task_details

            # Calculate how many seconds this task is already covered
            # by time slots that are already 'on'.
            already_covered_duration = 0
            for t in range(start_i, end_i + 1):
                if time_on[t]:
                    already_covered_duration += 1

            # Calculate how many more seconds this task needs to run.
            remaining_needed_duration = duration_i - already_covered_duration

            # If it's already fully covered, move to the next task.
            if remaining_needed_duration <= 0:
                continue

            # This task needs more time. We need to turn on the computer
            # for 'remaining_needed_duration' additional seconds.
            # Greedily pick the latest available time slots within the task's range [start_i, end_i].
            # Iterate from end_i downwards to start_i.
            for t in range(end_i, start_i - 1, -1):     # From end_i down to start_i (inclusive)
                if not time_on[t]:  # If this time slot is not yet 'on'
                    time_on[t] = True   # Turn on the computer at this time slot
                    total_computer_on_time += 1  # Increment total on-time, as we've just turned on a new slot
                    remaining_needed_duration -= 1  # One second of this task's need is met

                    if remaining_needed_duration == 0:
                        break   # This tasks needs are now fully met, no need to schedule more for it

        return total_computer_on_time