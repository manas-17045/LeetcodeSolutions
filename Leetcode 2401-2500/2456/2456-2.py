# Leetcode 2456: Most Popular Video Creator
# https://leetcode.com/problems/most-popular-video-creator/
# Solved on 17th of September, 2025
from collections import defaultdict


class Solution:
    def mostPopularCreator(self, creators: list[str], ids: list[str], views: list[int]) -> list[list[str]]:
        """
        Finds the most popular creator(s) and their most popular video.

        Args:
            creators (list[str]): A list of creator names for each video.
            ids (list[str]): A list of video IDs.
            views (list[int]): A list of view counts for each video.
        Returns:
            list[list[str]]: A list of lists, where each inner list contains a popular creator's name
                             and the ID of their most popular video.
        """
        # Total views per creator
        total = defaultdict(int)
        # Best video info per creator
        best = {}

        n = len(creators)
        for i in range(n):
            c = creators[i]
            vId = ids[i]
            v = views[i]

            total[c] += v

            if c not in best:
                best[c] = (v, vId)
            else:
                cur_max, cur_id = best[c]
                # Update if this video has more views, or equal views but lexicographically smaller id
                if v > cur_max or (v == cur_max and vId < cur_id):
                    best[c] = (v, vId)

        # Find highest popularity
        max_pop = 0
        for c, t in total.items():
            if t > max_pop:
                max_pop = t

        # Collect all creators with popularity == max_pop
        res = []
        for c, t in total.items():
            if t == max_pop:
                res.append([c, best[c][1]])

        return res