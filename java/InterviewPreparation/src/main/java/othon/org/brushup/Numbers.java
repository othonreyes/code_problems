package othon.org.brushup;

import lombok.extern.slf4j.Slf4j;

@Slf4j
public class Numbers {
    public static void main(String[] args) {
        int min = 5;
        int max = 2340;
        // Do a division of ints result in a double?
        double target = (min + max) / 2;
        log.info("(min + max) / 2 = {}", target);
        // No. Ends with an int number

        // what about casting it?
        target = (double) (min + max) / 2;// Yup, casting it does the trick
        log.info("(min + max) / 2 = {}", target);

        target = (double) (1 + 4) / 2;
        log.info("(min + max) / 2 = {}", target);

        // does a comparison sends a compiler warning
        if (1.0==1) {
            log.info("No, it doesn't");
        }

        // Exponents of 10
        for (int i = 0; i < 5; i++) {
            log.info("{}", Math.pow(10, i));
        }

    }
}
