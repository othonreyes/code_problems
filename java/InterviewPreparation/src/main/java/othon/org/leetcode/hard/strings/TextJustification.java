package othon.org.leetcode.hard.strings;

import lombok.extern.slf4j.Slf4j;
import lombok.var;

import java.util.ArrayList;
import java.util.List;

/**
 * Link:
 * <p>https://leetcode.com/problems/text-justification/
 * TODO:
 */

@Slf4j
public class TextJustification {
    public static void main(String[] args) {
        Solution s = new Solution();
        String[] input = {"Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"};
        int justification = 20;
        log.info("{}", s.fullJustify(input, justification));
    }

    static class Solution {
        List<String> results = new ArrayList<>();
        public List<String> fullJustify(String[] words, int maxWidth) {
            List<String> buffer = new ArrayList<>();
            int currentWordsWidth = 0;
            int currentWidth = 0;
            int i = 0;
            while (i<words.length) {
                String w = words[i];
                if (currentWidth >= maxWidth || currentWidth + w.length() >= maxWidth ) {
                    justify(buffer, currentWordsWidth, maxWidth);
                    currentWordsWidth = 0;
                    currentWidth = 0;
                    buffer.clear();
                    continue;
                }
                // take the word
                currentWidth += w.length() + 1;
                currentWordsWidth += w.length();
                buffer.add(w);

                i += 1;
            }
            leftJustify(buffer, currentWordsWidth, maxWidth);
            return results;
        }

        void leftJustify(List<String> buffer, int currentWordsWidth, int maxWidth) {
            StringBuffer sb = new StringBuffer();
            for (int i = 0; i<buffer.size(); i++) {
                sb.append(buffer.get(i));
                if (i< buffer.size() -1) {
                    spaceGen(1, sb);
                }
            }
            int extraSpaces = maxWidth - sb.length();
            spaceGen(extraSpaces, sb);
            results.add(sb.toString());
        }

        void justify(List<String> buffer, int currentWordsWidth, int maxWidth) {
            if (buffer.size() == 1) {
                leftJustify(buffer, currentWordsWidth, maxWidth);
                return;
            }
            int spaces = maxWidth - currentWordsWidth;
            int spaceSize = spaces / (buffer.size() - 1);

            StringBuffer sb = new StringBuffer();
            sb.append(buffer.get(0));


            if (spaces %2 != 0)
                spaceGen(spaceSize + 1, sb);
            else
                spaceGen(spaceSize, sb);


            for (int i =1; i<buffer.size(); i++) {
                sb.append(buffer.get(i));
                if (i< buffer.size() -1) {
                    spaceGen(spaceSize, sb);
                }
            }
            results.add(sb.toString());
        }
        void spaceGen(int spaceSize, StringBuffer sb) {
            for (int i =0; i<spaceSize; i++) {
                sb.append(" ");
            }
        }
    }

}
