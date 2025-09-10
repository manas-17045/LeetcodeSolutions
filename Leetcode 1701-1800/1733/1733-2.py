# Leetcode 1733: Minimum Number of People to Teach
# https://leetcode.com/problems/minimum-number-of-people-to-teach/
# Solved on 10th of September, 2025
class Solution:
    def minimumTeachings(self, n: int, languages: list[list[int]], friendships: list[list[int]]) -> int:
        """
        Calculates the minimum number of users that need to be taught a new language
        to resolve all communication issues among friends.
        :param n: The total number of languages available (1 to n).
        :param languages: A list of lists, where languages[i] is a list of languages user i+1 knows.
        :param friendships: A list of pairs [u, v] indicating a friendship between user u and user v.
        :return: The minimum number of users to teach.
        """
        # Number of users
        m = len(languages)
        # Convert each user's languages to a set
        lang_sets = [set()] + [set(l) for l in languages]

        # Find friendships where users cannot communicate (no common language)
        bad_users = set()
        for u, v in friendships:
            if lang_sets[u].isdisjoint(lang_sets[v]):
                bad_users.add(u)
                bad_users.add(v)

        # If no bad friendships, no need to tach anyone
        if not bad_users:
            return 0

        # Count how many bad users already know each language
        known_count = [0] * (n + 1)
        for users in bad_users:
            for lang in lang_sets[users]:
                known_count[lang] += 1

        total_bad = len(bad_users)
        ans = min(total_bad - known_count[lang] for lang in range(1, (n + 1)))
        return ans