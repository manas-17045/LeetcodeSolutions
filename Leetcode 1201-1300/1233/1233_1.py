# Leetcode 1233: Remove Sub-Folders from the Filesystem
# https://leetcode.com/problems/remove-sub-folders-from-the-filesystem/
# Solved on 19th of July, 2025
class Solution:
    def removeSubfolders(self, folder: list[str]) -> list[str]:
        """
        Removes all sub-folders from a given list of folder paths.
        :param folder: A list of folder paths (strings).
        :return: A list of root folder paths after removing sub-folders.
        """
        folder.sort()

        rootFolders = [folder[0]]

        for currentFolder in folder[1:]:
            lastFolder = rootFolders[-1]

            # Check if current folder is a sub-folder of the last identified root.
            if not currentFolder.startswith(lastFolder + '/'):
                rootFolders.append(currentFolder)

        return rootFolders