package othon.org.brushup;

import lombok.extern.slf4j.Slf4j;

@Slf4j
public class BitVectors {
    public static void main(String[] args) {
        int v = 0;
        for (int i = 0; i < 32; i++) {
            v |= 1<<i;
            log.info("{}-{}-{}", i, v, Integer.toString(v,2));
        }
        int k = 35;
        log.info("{}-{}-{}", k, k%32, Integer.toString((k&0x1F),2));

        String T = "abc";
        int x = ~T.length() & 1;
        log.info("{}", x);

        for (int i = 0; i < 5; i++) {
            log.info("{}-{}-{}", i, (i&1), (~i & 1));
        }
    }
}
