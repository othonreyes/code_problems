package othon.org.leetcode.medium.graph;

import lombok.extern.slf4j.Slf4j;
import lombok.var;

import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Queue;
import java.util.Set;

/**
 * Link: https://leetcode.com/problems/course-schedule-ii
 * <p>
 * Input: 2, [[1,0]]
 * Output: [0,1]
 * Explanation: There are a total of 2 courses to take. To take course 1 you should have finished
 *              course 0. So the correct course order is [0,1]
 */

@Slf4j
public class CourseScheduleII {
    public static void main(String[] args) {
        Solution s = new Solution();
//        log.info("", s.findOrder(2,new int[][]{{1,0}}));
        log.info("", s.findOrder(2,new int[][]{{0,1},{0,2},{1,2}}));
    }

    static class Solution {
        int numCourses;
        Map<Integer, List<Integer>> dependants;
        int index;
        public int[] findOrder(int numCourses, int[][] prerequisites) {
            if (numCourses == 1) {
                return new int[]{0};
            }
            this.numCourses = numCourses;
            //Map<Integer, List<Integer>> graph = new HashMap<>();
            dependants = new HashMap<>();
            for (int i=0; i<numCourses; i++) {
                // graph.computeIfAbsent(i, key->new ArrayList<>());
                dependants.computeIfAbsent(i, key->new ArrayList<>());
            }

            // build graph
            for(int[] edge: prerequisites) {
                //graph.computeIfAbsent(edge[1], key->new ArrayList<>()).add(edge[0]);
                dependants.get(edge[0]).add(edge[1]);
            }

            int[] output = new int[numCourses];
            index = 0;
            boolean[] visited = new boolean[numCourses];

            for (int i=0; i < numCourses; i++) {
                boolean valid = dfs(output, i, visited, null);
                if (!valid) {
                    return new int[]{};
                }
            }
            return output;
        }
        boolean dfs(int[] output, int course, boolean[] visited, boolean[] added) {
            if (added != null && added[course]) {
                return false;
            }
            if (visited[course]) {
                return true;
            }
            if (added == null) {
                added = new boolean[numCourses];
            }
            visited[course] = true;
            added[course] = true;
            for (Integer nextCourse : dependants.getOrDefault(course, Collections.emptyList())) {
                if (!visited[nextCourse]) {
                    boolean valid = dfs(output, nextCourse, visited, added);
                    if (!valid) {
                        return false;
                    }
                }
            }
            output[index++] = course;
            return true;
        }

//     public int[] findOrder(int numCourses, int[][] prerequisites) {
//         if (numCourses == 1) {
//             return new int[]{0};
//         }
//         Map<Integer, List<Integer>> dependants = new HashMap<>();
//         Map<Integer, List<Integer>> graph = new HashMap<>();

//         // build graph
//         for(int[] edge: prerequisites) {
//             graph.computeIfAbsent(edge[1], key->new ArrayList<>()).add(edge[0]);
//             dependants.computeIfAbsent(edge[0], key->new ArrayList<>()).add(edge[1]);
//         }
//         int[] output = new int[numCourses];
//         int index = 0;
//         // find the node with no dependants
//         int starterCourse = Integer.MIN_VALUE;
//         for (int node : dependants.keySet()) {
//             for (Integer deptCourse : dependants.get(node)) {
//                 if (!dependants.containsKey(deptCourse)) {
//                     starterCourse = deptCourse;
//                     break;
//                 }
//             }
//         }

//         //do BFS to find all courses
//         Set<Integer> visited = new HashSet<>();
//         Queue<Integer> q = new ArrayDeque<>();
//         q.offer(starterCourse);
//         while (!q.isEmpty()) {
//             int course = q.poll();
//             visited.add(course);
//             output[index++] = course;
//             if (index == numCourses) {
//                 break;
//             }
//             // List<Integer> adjacent = graph.getOrDefault(course, Collections.emptyList());
//             for (Integer nextCourse : graph.getOrDefault(course, Collections.emptyList())) {
//                 if (nextCourse != null && !visited.contains(nextCourse)) {
//                     q.offer(nextCourse);
//                 }
//             }
//         }
//         return output;
//     }
    }
}
