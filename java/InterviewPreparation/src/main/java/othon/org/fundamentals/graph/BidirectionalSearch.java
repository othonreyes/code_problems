package othon.org.fundamentals.graph;


import lombok.extern.slf4j.Slf4j;

import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Queue;

@Slf4j
public class BidirectionalSearch {
    public static void main(String[] args) {
        int[][] graphNodes = {
                {6},
                {5,6}, // 2
                {5,4}, // 3
                {4},

                {7,3,2}, // 4
                {7,8,2,1}, // 5
                {8,0,1}, // 6

                {9,4,5}, // 7
                {9,5,6}, // 8

                {10,7,8}, //9

                {9,11,12}, // 10

                {10, 13, 14}, // 11
                {10, 14, 15}, // 12

                {11, 16, 17}, // 13
                {11, 12, 17, 18}, // 14
                {12, 18, 19}, // 12

                {13}, // 16
                {13, 14}, // 17
                {14, 15}, // 18
                {15}, // 19
        };

        Map<Integer, List<Integer>> graph = new HashMap<>();

        // build the graph
        for (int i = 0; i < graphNodes.length; i++) {
            graph.computeIfAbsent(i, k -> new ArrayList<>());
            for (int j = 0; j <graphNodes[i].length; j++) {
                graph.get(i).add(graphNodes[i][j]);
            }
        }

        log.info("Path: {}", biSearch(graph, 2,17));
    }

    private static List<Integer> biSearch(Map<Integer, List<Integer>> graph, int nodea, int nodeb) {
        Queue<Integer> qa = new ArrayDeque<>();
        boolean[] visiteda = new boolean[graph.size()];
        Integer[] parenta = new Integer[graph.size()];
        visiteda[nodea] = true;
        qa.offer(nodea);

        Queue<Integer> qb = new ArrayDeque<>();
        boolean[] visitedb = new boolean[graph.size()];
        Integer[] parentb = new Integer[graph.size()];
        visitedb[nodeb] = true;
        qb.offer(nodeb);

        List<Integer> path = Collections.emptyList();
        while(!qa.isEmpty() && !qb.isEmpty()) {
            int a = qa.poll();
            int b = qb.poll();
            log.info("Processing node {} & {}", a, b);
            bfs(graph, a, qa, visiteda, parenta);
            bfs(graph, b, qb, visitedb, parentb);
            Integer intersecting = isIntersecting(visiteda, visitedb);
            log.info("Intersecting node {}", intersecting);
            while (intersecting != null) {
                // generate the path
                return generatePath(intersecting, parenta, parentb);
            }
        }

        return path;
    }

    private static List<Integer> generatePath(Integer intersecting, Integer[] parenta, Integer[] parentb) {
        List<Integer> path = new ArrayList<>();
        path.add(intersecting);
        Integer i = intersecting;
        while (parenta[i] != null) {
            path.add(parenta[i]);
            i = parenta[i];
        }
        Collections.reverse(path);

        i = intersecting;
        while (parentb[i] != null) {
            path.add(parentb[i]);
            i = parentb[i];
        }
        return path;
    }

    private static Integer isIntersecting(boolean[] visiteda, boolean[] visitedb) {
        for (int i = 0; i < visiteda.length; i++) {
            if (visiteda[i] && visitedb[i]) {
                return i;
            }
        }
        return null;
    }

    private static void bfs(Map<Integer, List<Integer>> graph, int a, Queue<Integer> q, boolean[] visited, Integer[] parent) {
        for (Integer adjacent : graph.get(a)) {
            if (!visited[adjacent]) {
                visited[adjacent] = true;
                parent[adjacent] = a;
                q.offer(adjacent);
            }
        }
    }


}
