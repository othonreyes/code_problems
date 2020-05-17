package othon.org.interviews.ctci.chapter_10_sorting;

import lombok.extern.slf4j.Slf4j;

import java.util.Arrays;

@Slf4j
public class FindDuplicates {
    public static void main(String[] args) {
        int [] arr = new int[]{1,5,8,3,4,6,5,2,9,17};
        BitSet st = new BitSet();
        Arrays.stream(arr).forEach(x -> {
            if (st.get(x)) {
                log.info("Repeated {}", x);
            } else {
                st.set(x);
            }
        });
    }

    static class BitSet {
        int[] set = new int[1024];

        boolean get(int x) {
            int pos = x >> 5; // divide by 32;
            int offset = x&0x1F; // modulus 32
            // to the stored value, 0 or 1, comapre with 0 to check if it exist

            //return (set[pos]<<offset) == 1; / /doesn't work because we are comparing a bit not the whole value

            // the & (AND) will compare the right bit because we are shifting it to the left regardless if the other
            // bits are set or not
            log.info("Get {}={}",x, Integer.toBinaryString(set[pos]));
//            return (set[pos] & (1<<offset)) == 1; // Didn't work because is not comparing against 1 in int
            return (set[pos] & (1<<offset)) != 0;
        }

        void set(int x) {
            int pos = x >> 5; // divide by 32;
            int offset = x&0x1F; // modulus 32

//            set[pos] = 1<<offset; // Doesn't work because it overrides the previous bits that are set
            set[pos] |= 1<<offset;
            log.info("Set {}={}",x, Integer.toBinaryString(set[pos]));
        }
    }
}
