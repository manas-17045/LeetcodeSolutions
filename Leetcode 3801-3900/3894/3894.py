# Leetcode 3894: Traffic Signal Color
# https://leetcode.com/problems/traffic-signal-color/
# Solved on 19th of April, 2026
class Solution:
    def trafficSignal(self, timer: int) -> str:
        """
        Determines the traffic signal color based on the timer value.
        :param timer: int representing the time elapsed.
        :return: str representing the color of the signal.
        """
        if timer == 0:
            return "Green"
        if timer == 30:
            return "Orange"
        if 30 < timer <= 90:
            return "Red"

        return "Invalid"