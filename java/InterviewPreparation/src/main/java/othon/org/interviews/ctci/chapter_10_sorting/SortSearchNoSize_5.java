package othon.org.interviews.ctci.chapter_10_sorting;

import lombok.extern.slf4j.Slf4j;
import lombok.val;

import java.util.Arrays;

@Slf4j
public class SortSearchNoSize_5 {

    public static void main(String[] args) {
        int[] arr = {1,2,3,4,5,6,8,9,10,11};
        val list = new MyList(arr);
        log.info("{}", search(12, list));
        log.info("{}", search(3, list));
    }

    static class MyList {
        int[] arr;
        MyList(int[] arr) {
            this.arr = arr;
            Arrays.sort(arr);
        }
        int elementAt(int ix) {
            return ix<arr.length? arr[ix] : -1;
        }
    }

    static int search(int val, MyList list) {
        int end = jumpSearchSize(list);
        int start = 0;
        while (start<end) {
            int middle = (start + end) / 2;
            int valMiddle = list.elementAt(middle);
            if (valMiddle == val) {
                return middle;
            }
            if (valMiddle  < val) {
                start = middle + 1;
            }
            if (valMiddle > val) {
                end = middle - 1;
            }
        }
        return -1;
    }

    private static int jumpSearchSize(MyList list) {
        int jump = 1;
        // exponential jump
        for (; list.elementAt(jump)!= -1; jump *= 2);

        int i = jump;
        for (; list.elementAt(i) == -1; i--);
        return i;
    }
}
