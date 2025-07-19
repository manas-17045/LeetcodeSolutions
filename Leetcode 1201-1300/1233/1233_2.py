# Leetcode 1233: Remove Sub-Folders from the Filesystem
# https://leetcode.com/problems/remove-sub-folders-from-the-filesystem/
# Solved on 19th of July, 2025
class Solution:
    def removeSubfolders(self, folder: list[str]) -> list[str]:
        """
        Removes all subfolders from a given list of folders.
        :param folder: A list of folder paths.
        :return: A list of folder paths with subfolders removed.
        """
        # Sort so that any parent folder comes immediately before its subfolders
        folder.sort()

        res = []
        for f in folder:
            # If res is empty, or f is not a subfolder of the last folder in res, then we keep f.
            if not res or not f.startswith(res[-1] + "/"):
                res.append(f)

        return res