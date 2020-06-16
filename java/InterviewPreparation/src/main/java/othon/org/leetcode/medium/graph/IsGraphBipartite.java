package othon.org.leetcode.medium.graph;

import lombok.extern.slf4j.Slf4j;
import lombok.var;
import othon.org.leetcode.utils.Deserializer;

import java.util.HashMap;
import java.util.HashSet;
import java.util.LinkedList;
import java.util.Map;
import java.util.Set;

/**
 * Link: https://leetcode.com/explore/interview/card/facebook/52/trees-and-graphs/3028/
 * <p>
 * Given an undirected graph, return true if and only if it is bipartite.
 *
 * Recall that a graph is bipartite if we can split it's set of nodes into two independent subsets A and B such that every edge in the graph has one node in A and another node in B.
 *
 * The graph is given in the following form: graph[i] is a list of indexes j for which the edge between nodes i and j exists.  Each node is an integer between 0 and graph.length - 1.  There are no self edges or parallel edges: graph[i] does not contain i, and it doesn't contain any element twice.
 */

@Slf4j
public class IsGraphBipartite {
    public static void main(String[] args) {
        Solution s = new Solution();
        var input = Deserializer.toIntMatrix("[[1,3], [0,2], [1,3], [0,2]]");
        boolean result = s.isBipartite(input);
        log.info("{}", result);
    }

    static class Solution {
        Map<Integer, int[]> edges = new HashMap<>();
        public boolean isBipartite(int[][] graph) {
            // put the edges in the map
            LinkedList<Integer> nums = new LinkedList<>();
            Set<Integer> A = new HashSet<>();
            for (int i = 0; i< graph.length; i++) {
                edges.put(i, graph[i]);
                nums.add(i);
                A.add(i);
            }

            Set<Integer> B = new HashSet<>();
            return checkGraph(nums, A, B);
        }
        boolean checkGraph(LinkedList<Integer> nums, Set<Integer> A, Set<Integer> B) {
            if (nums.isEmpty()) {
                return false;
            }
            int length = nums.size();
            boolean result = false;
            for (int i = 0; i < length && !result; i++) {
                int node = nums.removeFirst();
                A.remove(node);
                B.add(node);
                // check all edges;
                result = checkEdges(A, B) || checkGraph(nums, A, B);

                // backtrack
                nums.addLast(node);
                B.remove(node);
                A.add(node);
            }
            return result;
        }

        boolean checkEdges(Set<Integer> A, Set<Integer> B) {
            if (A.isEmpty() || B.isEmpty()) {
                return false;
            }
            for (Map.Entry<Integer, int[]> entry : edges.entrySet()) {
                int node1 = entry.getKey();
                for (int node2: entry.getValue()) {
                    boolean r = A.contains(node1) && B.contains(node2) || A.contains(node2) && B.contains(node1);
                    if (!r) return false;
                }
            }
            return true;
        }
    }
}
