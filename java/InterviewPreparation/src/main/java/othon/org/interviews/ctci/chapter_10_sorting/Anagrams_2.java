package othon.org.interviews.ctci.chapter_10_sorting;

import lombok.extern.slf4j.Slf4j;

import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

@Slf4j
public class Anagrams_2 {
    public static void main(String[] args) {
        String[] anagrams = new String[]{"evil",
                "tap", "a gentleman",
                "angered" ,
                "pat", "vile",
                "elegant man", "eleven plus two","enraged", "twelve plus one"};
        log.info("{}", anagrams);
        Arrays.sort(anagrams, (o1, o2) -> {
            Map<Character, Integer> count = new HashMap<>();
            for (char c:o1.toCharArray()){
                if (c!= ' ') {
                    count.put(c, count.getOrDefault(c, 0) + 1);
                }
            }

            int extraSize = 0;
            for (char c:o2.toCharArray()){
                if (c == ' ') {
                    continue;
                }
                if (count.containsKey(c)) {
                    count.put(c, count.get(c ) - 1);
                    if (count.get(c) == 0) {
                        count.remove(c);
                    }
                } else {
                    extraSize += 1;
                }
            }
            int finalSize = count.size();
            return count.size() == 0? 0: count.size() -extraSize;
        });
        log.info("{}", anagrams);
    }
}
