package othon.org.leetcode;

import java.util.Arrays;
import java.util.PriorityQueue;

public class MeetingRooms2 {

    public static void main(String[] args) {
        int [][] intervals = { {0,30}, {5,10}, {20, 30} };
        System.out.println("Meeting rooms "  + meetings(intervals));
    }

    private static int meetings(int[][] intervals) {
        Arrays.sort(intervals, (a,b) -> a[0] - b[0]);
        // Compare based on when the meeting finishes. Meeting that finishes
        // Earlier should be at the top
        PriorityQueue<int[]> q = new PriorityQueue<>((o1, o2) -> o1[1] - o2[1]);
        for (int i = 0; i < intervals.length; i ++) {
            //The meeting that finishes first is always at the top, let's call firt meeting.
            // If our i-th meeting starts after the first meeting then we can remove the
            // first meeting.
            if (q.peek() != null &&
                q.peek()[1]<intervals[i][0]) {
                q.poll();
            }
            // Add the meeting so we can say that a room is in use.
            q.add(intervals[i]);
        }
        // Return the total of rooms used.
        return q.size();
    }
}
