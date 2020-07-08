package othon.org.utils;

import java.util.HashSet;
import java.util.Random;
import java.util.Set;

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

    public static int[] createUnorderedUniqueElemArray(int  size, int limit) {
        if (size > limit) {
            throw new IllegalArgumentException("size should be smaller or equals than limit");
        }
        Random random = new Random();
        int[] arr = new int[size];

        for (int i=0; i<size; i++) {
            arr[i] = random.nextInt(limit);
        }

        // verify that they are unique
        for (int i = 0; i < 10; i++) {
            Set<Integer> known = new HashSet<>();
            for (int j = 0; j < arr.length; j++) {
                if (!known.contains(arr[j])) {
                    known.add(arr[j]);
                } else {
                    arr[j] = newNumber(arr, j, random, known, limit);
                }
            }
        }

        return arr;
    }

    private static int newNumber(int[] arr, int j, Random random, Set<Integer> known, int limit) {
        for (int i = 0; i < 20; i++) {
            int nextInt = random.nextInt(limit);
            if (!known.contains(nextInt)) {
                return nextInt;
            }
        }
        // couldn't update the value so it's going to keep the same value
        return arr[j];
    }
}
