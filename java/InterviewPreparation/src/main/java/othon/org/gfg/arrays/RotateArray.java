package othon.org.gfg.arrays;

import java.util.Arrays;

/**
 * Possible solutions
 * 1. 2ble for
 * 2. 2ble for but descending
 * 3. One iteration but with extra array
 * 4. 2 iterations but inverting array in place.
 * 5. Rotate with offset
 */
public class RotateArray {

    /*
    TODO:
    - Add junit 5 to assert arrays
    - generate random inputs and validate,
        - generate random inputs of any size.
        - Add edge cases.
        - Implement the naive solution to generate the expectedArray
     */
    public static void main(String[] args) {
        int arr[] = { 1, 2, 3, 4, 5, 6, 7 };
        int wanted[] = { 3, 4, 5, 6, 7, 1, 2 };
        int positions = 2;
        rotateWithOffset(arr, positions);
        System.out.println(Arrays.toString(wanted) + " "+ Arrays.toString(arr));
    }

    /*
        int arr[] = { 1, 2, 3, 4, 5, 6, 7 };
        int arr[] = { 3, 2, 6, 4, 5, 1, 7 };
        int arr[] = { 3, 4, 6, 7, 5, 1, 2 };
        int arr[] = { 3, 4, 5, 6, 7, 1, 2 };
     */
    private static void rotateWithOffset(int[] arr, int positions) {
        int begining = 0;
        int offset = begining + positions;
        // Have an offset and start swapping positions in the array
        for (int i = arr.length - positions; i < arr.length; i++) {
            int temp = arr[begining];
            arr[begining] = arr[offset];
            arr[offset] = arr[i]; // We are going to leave the array with elements out of order because we are storing the ith element in the offset
            arr[i] = temp;
            begining += 1;
            offset += 1;
        }

        // Re order the array from where the offset started until the we know for sure that the array is rotated
        for (int i = begining; i < arr.length - positions; i++) {
            int temp = arr[arr.length - positions - 1];
            arr[arr.length - positions - 1] = arr[i];
            arr[i] = temp;
        }
    }
}

