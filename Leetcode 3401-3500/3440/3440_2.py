# Leetcode 3440: Reschedule Meetings for Maximum Free Time II
# https://leetcode.com/problems/reschedule-meetings-for-maximum-free-time-ii/
# Solved on 10th of July, 2025
from collections import Counter


class Solution:
    def maxFreeTime(self, eventTime: int, startTime: list[int], endTime: list[int]) -> int:
        """
        Calculates the maximum free time achievable by strategically placing an additional event.

        The problem asks us to find the maximum free time (largest single gap) we can create
        by inserting an additional event of a given duration 'd' into an existing schedule.
        We can either place the event in an existing gap or replace an existing event.

        Args:
            eventTime (int): The total duration of the timeline (e.g., 24 hours).
            startTime (list[int]): A list of start times for existing events.
            endTime (list[int]): A list of end times for existing events.

        Returns:
            int: The maximum free time (largest single gap) achievable.
        """
        n = len(startTime)
        gaps = [0] * (n + 1)
        gaps[0] = startTime[0]
        for i in range(1, n):
            gaps[i] = startTime[i] - endTime[i - 1]
        gaps[n] = eventTime - endTime[-1]

        cnt = Counter(gaps)
        top_vals = sorted(cnt.keys(), reverse=True)[:4]
        idx_of = {v:i for i, v in enumerate(top_vals)}
        counts = [cnt[v] for v in top_vals]

        best = top_vals[0] if top_vals else 0

        def largest_two_after_removal(rem: list[int]):
            first = 0
            while first < len(rem) and rem[first] == 0:
                first += 1
            g1 = top_vals[first] if first < len(rem) else 0

            second = first + 1
            while second < len(rem) and rem[second] == 0:
                second += 1
            g2 = top_vals[second] if second < len(rem) else 0
            return g1, g2

        # For each meeting i, remove its two neighboring gaps and insert the merged gap
        for i in range(n):
            d = endTime[i] - startTime[i]
            gL = gaps[i]
            gR = gaps[i + 1]
            gM = gL + d + gR

            # Build a tiny local copy of the top-4 counts, then subtract any removals
            rem_counts = counts[:]
            if gL in idx_of:
                rem_counts[idx_of[gL]] -= 1
            if gR in idx_of:
                rem_counts[idx_of[gR]] -= 1

                # Find the top two gaps among the "other" free slots (before reinserting)
                FO0, SO0 = largest_two_after_removal(rem_counts)

                # Now include the merged gap gM as a candidate
                FO = FO0 if FO0 >= gM else gM
                if gM >= FO0:
                    SO = FO0
                else:
                    # FO0 > gM
                    SO = gM if gM >= SO0 else SO0

                # We can only re‐insert meeting if there's some gap ≥ d
                if FO < d:
                    continue

                # Ff there is a second gap ≥ d, we can put the meeting there
                if SO >= d:
                    cand = FO
                else:
                    # otherwise we must split the only large gap of size FO
                    cand = max(SO, FO - d)

                if cand > best:
                    best = cand

            return best