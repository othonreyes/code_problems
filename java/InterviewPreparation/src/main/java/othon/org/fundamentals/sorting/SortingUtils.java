package othon.org.fundamentals.sorting;

import java.util.Random;

public class SortingUtils {
    public static int[] createUnorderedArray() {
        return createUnorderedArray(20, 1000);
    }

    public static int[] createUnorderedArray(int  size, int limit) {
        Random random = new Random();
        int[] arr = new int[size];

        for (int i=0; i<size; i++) {
            arr[i] = random.nextInt(limit);
        }
        return arr;
    }
}
