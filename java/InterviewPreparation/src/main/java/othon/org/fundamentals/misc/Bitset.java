package othon.org.fundamentals.misc;

import lombok.extern.slf4j.Slf4j;

@Slf4j
public class Bitset {

    public static void main(String[] args) {
        Bitset bs = new Bitset();
        bs.set(5);
        log.info("Has 5? {}", bs.get(5));
        log.info("Has 4? {}", bs.get(4));
        bs.set(0);
        bs.set(31);
        bs.set(32);
        bs.set(100);
        log.info("Has 0? {}", bs.get(0));
        log.info("Has 31? {}", bs.get(31));
        log.info("Has 32? {}", bs.get(32));
        log.info("Has 100? {}", bs.get(100));
        log.info("Has 1000? {}", bs.get(1000));
    }

    int[] set = new int[69273666]; // 2^31/31

    void set(int x) {
        // modu
        int section = x / 32; // find the subset
        int mod = x%32;
        set[section] |= 1<<mod;

        int pos = x >> 5; // divide by 32
        int offset = x & 0X1F; //mod 32
    }

    boolean get(int x) {
        int section = x / 32; // find the subset
        int mod = x%32;
        return (set[section] & 1<<mod) != 0;
    }
}
