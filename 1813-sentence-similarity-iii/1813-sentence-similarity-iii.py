class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        if sentence1 == sentence2:
            return True
        if len(sentence1) < len(sentence2):
            sentence1, sentence2 = sentence2,sentence1
        sentence1 = sentence1.split(' ')
        sentence2 = sentence2.split(' ')
        for i in range(len(sentence1)):
            for j in range(i,len(sentence1)+1):
                if sentence1[:i] + sentence1[j:]== sentence2:
                    return True
        return False