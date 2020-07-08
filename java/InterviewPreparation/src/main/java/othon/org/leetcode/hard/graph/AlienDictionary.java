package othon.org.leetcode.hard.graph;

import lombok.extern.slf4j.Slf4j;
import lombok.var;

import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Queue;

/**
 * Link: https://leetcode.com/problems/alien-dictionary/
 * <p>
 * TODO:
 */

@Slf4j
public class AlienDictionary {
    public static void main(String[] args) {
        Solution s = new Solution();
        String[] input = {
                "wrt",
                "wrf",
                "er",
                "ett",
                "rftt"};
        log.info("{}", s.alienOrder(input));
    }

    static class Solution {
        public String alienOrder(String[] words) {
            // create a graph and the indegree
            Map<Character, List<Character>> graph = new HashMap<>();
            Map<Character, Integer> indegree = new HashMap<>();
            for (String w: words) {
                for (int i = 0; i < w.length(); i++) {
                    graph.put(w.charAt(i), new ArrayList<>());
                    indegree.put(w.charAt(i), 0);
                }
            }

            // Iterate over the words
            for (int i = 0; i < words.length - 1; i++) {
                String word1 = words[i];
                String word2 = words[i + 1];
                if (word1.length() > word2.length() && word1.startsWith(word2)) {
                    return ""; // invalid result as word2 is a prefix of word 1
                }
                for (int j = 0; j < Math.min(word1.length(), word2.length()); j++) {
                    if (word1.charAt(j) != word2.charAt(j)) {
                        graph.get(word1.charAt(j)).add(word2.charAt(j));
                        indegree.put(word2.charAt(j), indegree.get(word2.charAt(j)) + 1);
                    }
                }
            }

            // BFS
            Queue<Character> q = new ArrayDeque<>();
            StringBuffer sb = new StringBuffer();
            for (Character c: graph.keySet()) {
                if (indegree.get(c) == 0) {
                    q.offer(c); // Add the chars that don't have a dependency
                }
            }

            // BFS usign topological sort
            while (!q.isEmpty()) {
                Character c = q.poll();
                sb.append(c);
                for (Character c2: graph.get(c)) {
                    // decrement the count
                    indegree.put(c2, indegree.get(c2) - 1);
                    if (indegree.get(c2) == 0) {
                        q.offer(c2);
                    }
                }
            }

            // check if it's valid by comparing the total characters found vs those added in the dictionary
            if (sb.length()!= indegree.size()) {
                return "";
            }
            return sb.toString();
        }
    }
}
