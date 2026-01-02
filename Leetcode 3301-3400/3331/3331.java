// Leetcode 3331: Find Subtree Sizes After Changes
// https://leetcode.com/problems/find-subtree-sizes-after-changes/
// Solved on 2nd of January, 2026
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class Solution {
    /**
     * Finds the subtree sizes after applying specific changes to the tree structure.
     * @param parent An array representing the parent of each node, where parent[i] is the parent of node i.
     * @param s A string where s.charAt(i) is the character associated with node i.
     * @return An array where sizes[i] is the size of the subtree rooted at node i in the modified tree.
     */
    public int[] findSubtreeSizes(int[] parent, String s) {
        int n = parent.length;
        List<Integer>[] originalTree = new ArrayList[n];
        List<Integer>[] newTree = new ArrayList[n];

        for (int i = 0; i < n; i++) {
            originalTree[i] = new ArrayList<>();
            newTree[i] = new ArrayList<>();
        }

        for (int i = 1; i < n; i++) {
            originalTree[parent[i]].add(i);
        }

        int[] ancestors = new int[26];
        Arrays.fill(ancestors, -1);

        buildNewTree(0, originalTree, newTree, parent, s, ancestors);

        int[] sizes = new int[n];
        calculateSubtreeSizes(0, newTree, sizes);

        return sizes;
    }

    private void buildNewTree(int node, List<Integer>[] originalTree, List<Integer>[] newTree, int[] parent, String s, int[] ancestors) {
        int charIndex = s.charAt(node) - 'a';
        int closestAncestor = ancestors[charIndex];

        if (node != 0) {
            int newParent = (closestAncestor != -1) ? closestAncestor : parent[node];
            newTree[newParent].add(node);
        }

        int previousAncestor = ancestors[charIndex];
        ancestors[charIndex] = node;

        for (int child : originalTree[node]) {
            buildNewTree(child, originalTree, newTree, parent, s, ancestors);
        }

        ancestors[charIndex] = previousAncestor;
    }

    private int calculateSubtreeSizes(int node, List<Integer>[] newTree, int[] sizes) {
        int size = 1;
        for (int child : newTree[node]) {
            size += calculateSubtreeSizes(child, newTree, sizes);
        }
        sizes[node] = size;
        return size;
    }
}