package othon.org.leetcode.medium.dp;

import lombok.extern.slf4j.Slf4j;

import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Queue;
import java.util.Set;

@Slf4j
public class LongestStringChain {

    public static void main(String[] args) {
        String[] input = {"a","b","ba","bca","bda","bdca"};
        Solution s = new Solution();
        log.info("{}", s.longestStrChain(input));
    }


    static class Solution {
        // graph approach doesn't work needs to be dp
        public int longestStrChain(String[] words) {
            Map<String, List<String>> graph = new HashMap<>();
            for (String w : words) {
                for (int i=0;i<w.length();i++) {
                    String s = w.substring(0, i) + w.substring( i + 1, w.length());
                    if (graph.containsKey(s)) {
                        graph.get(s).add(w);
                    }
                }
                graph.put(w, new ArrayList<>());
            }


            int ans = Integer.MIN_VALUE;
            Set<String> visited = new HashSet<>();
            Queue<String> q = new ArrayDeque<>();
            for (String w : words) {
                if (visited.contains(w)) {
                    continue;
                }
                int moves = 0;
                q.offer(w);
                while (!q.isEmpty()) {
                    String s = q.poll();
                    visited.add(s);
                    moves += 1;
                    ans = Math.max(ans, moves);
                    for (String a: graph.get(s)) {
                        if (visited.contains(a)) {
                            continue;
                        }
                        q.offer(a);
                    }
                }
            }
            return ans;
        }
    }

}
