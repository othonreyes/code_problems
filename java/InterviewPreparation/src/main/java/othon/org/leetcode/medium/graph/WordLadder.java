package othon.org.leetcode.medium.graph;

import lombok.extern.slf4j.Slf4j;
import lombok.var;
import othon.org.leetcode.utils.Deserializer;

import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Queue;
import java.util.Set;
import java.util.stream.Collectors;

/**
 * Link: https://leetcode.com/explore/featured/card/google/61/trees-and-graphs/3068/
 * Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:
 *
 *     Only one letter can be changed at a time.
 *     Each transformed word must exist in the word list.
 *
 * Note:
 *
 *     Return 0 if there is no such transformation sequence.
 *     All words have the same length.
 *     All words contain only lowercase alphabetic characters.
 *     You may assume no duplicates in the word list.
 *     You may assume beginWord and endWord are non-empty and are not the same.
 *
 * Example 1:
 *
 * Input:
 * beginWord = "hit",
 * endWord = "cog",
 * wordList = ["hot","dot","dog","lot","log","cog"]
 *
 * Output: 5
 *
 * Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
 * return its length 5.
 *
 * Example 2:
 *
 * Input:
 * beginWord = "hit"
 * endWord = "cog"
 * wordList = ["hot","dot","dog","lot","log"]
 *
 * Output: 0
 *
 * Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.
 *
 * <p>
 * TODO:
 */

@Slf4j
public class WordLadder {
    public static void main(String[] args) {
        Solution s = new Solution();
        List<String> wordList = Deserializer.toStringList("[\"hot\",\"dot\",\"dog\",\"lot\",\"log\",\"cog\"]");
        var result = s.ladderLength("hit", "cog", wordList);
        log.info("The input is {}", result);
    }

    static class Solution {
        public int ladderLength(String beginWord, String endWord, List<String> wordList) {
            Map<String, Set<String>> graph = new HashMap<>();
            for (int i = 0; i < wordList.size(); i++) {
                graph.computeIfAbsent(wordList.get(i), l->new HashSet());
                for (int j = 0; j < wordList.size(); j++) {
                    if (i==j) continue;
                    if (diffByOneChar(wordList.get(i), wordList.get(j))) {
                        graph.computeIfAbsent(wordList.get(j), l->new HashSet()).add(wordList.get(i));
                        graph.get(wordList.get(i)).add(wordList.get(j));
                    }
                }
            }
            // find related nodes that are diff by one word
            List<String> possibleNodes = findNodes(beginWord, wordList);

            int ans = Integer.MAX_VALUE;
            // BFS poossible nodes and keep the smallestValue
            for (String n: possibleNodes) {
                ans = Math.min(ans, bfs(endWord, n, graph));
            }
            return ans == Integer.MAX_VALUE? 0 : ans + 1;
        }

        boolean diffByOneChar(String s1, String s2) {
            int counter = 0;
            for (int i = 0; i < s1.length(); i++) {
                if (s1.charAt(i)!=s2.charAt(i))
                    counter += 1;
            }
            return counter <= 1;
        }

        List<String> findNodes(String beginWord, List<String> wordList) {
            return wordList.stream().filter(w -> diffByOneChar(beginWord, w))
                    .collect(Collectors.toList());
        }

        int bfs(String target, String node, Map<String, Set<String>> graph) {
            Set<String> visited = new HashSet<>();
            // TODO: (A)have a pair to keep track of the level i.e new Pair<>(node, 1)
            Queue<Pair> q = new ArrayDeque<>();
            q.offer(new Pair(node, 0));
            visited.add(node);
            int counter = Integer.MAX_VALUE;
            while (!q.isEmpty()) {
                Pair p =  q.poll();
                log.info("{}-{}", p.word, p.level);
                if (p.word.equals(target)) {
                    // TODO: (B) don't quit, keep iterating,but updated the min steps i.e. steps = Math.min(steps, node.getValue())
                    counter = Math.min(counter, p.level + 1);
                    continue;
                }
                for (String w: graph.get(p.word)) {
                    if (visited.contains(w)) {
                        continue;
                    }
                    // TODO: (C) Offer a new Pair<>(w, node.getValue() + 1)
                    visited.add(w);
                    q.offer(new Pair(w, p.level + 1));
                }
            }
            return counter;
        }

//        int bfs(String target, String node, Map<String, Set<String>> graph) {
//            Set<String> visited = new HashSet<>();
//            int counter = 0;
//            // TODO: (A)have a pair to keep track of the level i.e new Pair<>(node, 1)
//            Queue<String> q = new ArrayDeque<>();
//            q.offer(node);
//            visited.add(node);
//            while (!q.isEmpty()) {
//                String n = q.poll();
//                log.info("{}-{}", n, counter);
//                if (n.equals(target)) {
//                    // TODO: (B) don't quit, keep iterating,but updated the min steps i.e. steps = Math.min(steps, node.getValue())
//                    return counter + 1;
//                }
//                counter += 1;
//                for (String w: graph.get(n)) {
//                    if (visited.contains(w)) {
//                        continue;
//                    }
//                    // TODO: (C) Offer a new Pair<>(w, node.getValue() + 1)
//                    visited.add(w);
//                    q.offer(w);
//                }
//            }
//            return Integer.MAX_VALUE;
//        }
    }


    static class Pair {
        String word;
        int level;

        public Pair(String word, int level) {
            this.word = word;
            this.level = level;
        }
    }
}
