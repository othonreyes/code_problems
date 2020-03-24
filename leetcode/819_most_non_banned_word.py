from typing import List

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        # put the banned words in a set
        banned_set = set([x.lower() for x in banned])
        
        most_freq_word = ""
        frequency = 0
        from collections import Counter
        wc = Counter()
        
        delimiters = set([' ', '!', '?', ';', '\'', ',', '.'])
        
        start = -1
        end = 0
        n = len(paragraph)
        # iterate over the string
        for i in range(len(paragraph)):
            if start == -1 and ('a' <= paragraph[i] <= 'z' or 'A' <= paragraph[i] <= 'Z'):
                start = i
                continue
            #substring once we found a space or a punction mark
            if (paragraph[i] in delimiters or i == n -1) and start > -1:
                    if paragraph[i] in delimiters:
                        end = i
                    else:
                        end = n
                    # if end < start:
                    #     continue
                    word = paragraph[start:end].lower()
                    start = -1 # reset start
                    
                    # if the word is in the list of banned words then move on
                    if word in banned_set:
                        continue
                    # else update the map
                    wc[word] = 1 + wc[word]
                    
                    # if the updated word has a bigger count than our most frequent word
                    if wc[word] > frequency:
                        # then update the counter and the most grequent word
                        frequency = wc[word]
                        most_freq_word = word
        return most_freq_word

    """Doesn't work"""
    def mostCommonWord2(self, paragraph: str, banned: List[str]) -> str:
        # put the banned words in a set
        banned_set = set([x.lower() for x in banned])
        
        most_freq_word = ""
        frequency = 0
        from collections import Counter
        wc = Counter()
        
        delimiters = set([' ', '!', '?', ';', '\'', ',', '.'])
        
        start = -1
        end = 0
        n = len(paragraph)
        word = ""
        # iterate over the string
        for i in range(len(paragraph)):
            if ('a' <= paragraph[i] <= 'z' or 'A' <= paragraph[i] <= 'Z'):
                word += paragraph[i]
            elif len(word) > 0:
                word = word.lower()
                if word in banned_set:
                    word = ""
                    continue
                # else update the map
                wc[word] = 1 + wc[word]
                
                # if the updated word has a bigger count than our most frequent word
                if wc[word] > frequency:
                    # then update the counter and the most grequent word
                    frequency = wc[word]
                    most_freq_word = word
                word = ""
        return most_freq_word

if __name__ == "__main__":
    s = Solution()
    print(s.mostCommonWord("Bob. hIt, baLl", ["bob", "hit"]))
    print(s.mostCommonWord2("Bob. hIt, baLl", ["bob", "hit"]))