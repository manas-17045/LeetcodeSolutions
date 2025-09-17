# Leetcode 2456: Most Popular Video Creator
# https://leetcode.com/problems/most-popular-video-creator/
# Solved on 17th of September, 2025
from collections import defaultdict


class Solution:
    def mostPopularCreator(self, creators: list[str], ids: list[str], views: list[int]) -> list[list[str]]:
        """
        Finds the most popular creator(s) and their most viewed video.
        :param creators: A list of strings representing the creator of each video.
        :param ids: A list of strings representing the ID of each video.
        :param views: A list of integers representing the view count of each video.
        :return: A list of lists, where each inner list contains the name of a most popular creator and the ID of their most viewed video.
        """
        creatorPopularity = defaultdict(int)
        creatorMostViewed = {}
        highestPopularity = 0

        numVideos = len(creators)
        for i in range(numVideos):
            creator = creators[i]
            videoId = ids[i]
            viewCount = views[i]

            creatorPopularity[creator] += viewCount

            if creatorPopularity[creator] > highestPopularity:
                highestPopularity = creatorPopularity[creator]

            if creator not in creatorMostViewed:
                creatorMostViewed[creator] = (viewCount, videoId)
            else:
                currentMaxView, currentBestId = creatorMostViewed[creator]

                if viewCount > currentMaxView or (viewCount == currentMaxView and videoId < currentBestId):
                    creatorMostViewed[creator] = (viewCount, videoId)

        answer = []
        for creator, totalViews in creatorPopularity.items():
            if totalViews == highestPopularity:
                bestVideoId = creatorMostViewed[creator][1]
                answer.append([creator, bestVideoId])

        return answer