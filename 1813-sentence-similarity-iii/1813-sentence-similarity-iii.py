class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        deq1,deq2 = map(deque, (sentence1.split(), sentence2.split()))
        while deq1 and deq2 and deq1[0] == deq2[0]:
            deq1.popleft()
            deq2.popleft()
        while deq1 and deq2 and deq1[-1] == deq2[-1]:
            deq1.pop()
            deq2.pop()

        return not deq1 or not deq2