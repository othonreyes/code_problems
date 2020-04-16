package othon.org.brushup;

import java.util.PriorityQueue;

public class Queues {
    public static void main(String[] args) {
        // https://leetcode.com/problems/path-with-maximum-minimum-value/discuss/323927/Java-BFS-%2B-PQ

        // o2 - o1 reverse the otrder so maximum is on top
        PriorityQueue<Integer> q = new PriorityQueue<>((o1, o2) -> o2-o1);
        //o1 - o2 sorts from min to max
        // PriorityQueue<Integer> q = new PriorityQueue<>((o1, o2) -> o1-o2);
        q.offer(2);
        System.out.println(q.peek());

        int x = q.poll();
        q.offer(Math.min(x, 0));
        System.out.println(q.peek() + "-" + q.size());
        q.offer(Math.min(x, 2));
        System.out.println(q.peek() + "-" + q.size());

        x = q.poll();
        q.offer(Math.min(x, 4));
        System.out.println(q.peek() + "-" + q.size());
        q.offer(Math.min(x, 1));
        System.out.println(q.peek() + "-" + q.size());
    }
}
