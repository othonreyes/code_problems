package othon.org.fundamentals.sorting;

import java.util.Random;

public class SortingUtils {
    public static int[] createUnorderedArray() {
        Random random = new Random();
        int[] arr = new int[20];

        for (int i=0; i<20; i++) {
            arr[i] = random.nextInt(1000);
        }
        return arr;
    }
}
