package othon.org.leetcode.medium.graph;

import lombok.extern.slf4j.Slf4j;
import lombok.var;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;

/**
 * Link:
 * <p>
 * TODO: https://leetcode.com/problems/evaluate-division/
 */

@Slf4j
public class EvaluateDivision {
    public static void main(String[] args) {
        Solution s = new Solution();
        List<List<String>> equations = Arrays.asList(Arrays.asList("a", "b"), Arrays.asList("b", "c"));
        double[] values = new double[]{2.0, 3.0};
        List<List<String>> queries = Arrays.asList(Arrays.asList("b", "a"));
        log.info("{}", s.calcEquation(equations, values, queries));
    }

    static class Solution {
        public double[] calcEquation(List<List<String>> equations, double[] values, List<List<String>> queries) {
            // first build the matrix
            Map<String, List<Pair>> nodes = new HashMap<>();

            for (int i = 0; i < equations.size(); i ++ ) {
                String n1 = equations.get(i).get(0);
                String n2 = equations.get(i).get(1);
                double cost = values[i];
                nodes.computeIfAbsent(n1, key -> new ArrayList<>()).add(new Pair(n2, cost));
                nodes.computeIfAbsent(n2, key -> new ArrayList<>()).add(new Pair(n1, 1.0/cost));
            }

            double[] results = new double[queries.size()];
            for (int i = 0; i<queries.size(); i++) {
                String start = queries.get(i).get(0);
                String end = queries.get(i).get(1);
                if (!nodes.containsKey(start) || !nodes.containsKey(end)) {
                    results[i] = -1.0;
                    continue;
                }
                results[i] = evaluate(nodes, start, end);
            }
            return results;
        }

        class Pair {
            String node;
            double val;
            Pair (String n, double v) {
                node = n;
                val = v;
            }

            public boolean equals(Pair o) {
                if (o == null) return false;
                return node.equals(o.node);
            }

            public int hashCode() {return node.hashCode();}
        }

        double evaluate(Map<String, List<Pair>> g, String start, String end) {
            if (start.equals(end)) {
                return 1.0;
            }

            Set<String> visited = new HashSet<>();
            Double result = divide(start, end, g, 1.0, visited);
            if (result == null) {
                return -1.0;
            }
            return result;
        }

        Double divide(String start, String end, Map<String, List<Pair>> g, Double acc, Set<String> visited) {
            if (start.equals(end)) {
                return acc;
            }
            visited.add(start);
            Double result = null;
            for(Pair p : g.get(start)) {
                if (!visited.contains(p.node)) {
                    Double temp = acc * p.val;
                    result = divide(p.node, end, g, temp, visited);
                }
            }
            return result;
        }
    }
}
