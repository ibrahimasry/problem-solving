class Solution:
    def isItPossible(self, word1: str, word2: str) -> bool:
        set1 = set(word1)
        set2 = set(word2)
        if word1 == word2:
            return True
        if len(set2) > len(set1):
            set2  , set1 = set1 , set2
            word2 ,word1 = word1 , word2

        if abs(len(set1) - len(set2)) > 2:
            return False
        count1 = Counter(word1)
        count2 = Counter(word2)
        #different by only Two chars
        if len(set1) - len(set2) == 2:
                # add unique chars from big set to small one , if we can swap that char with chars that wont change the big
                #set  chars
                
                canSwap = any(True for c in set1 if count2[c] > 1 and count1[c] >= 1) 

                if not canSwap:
                    return False
                for c in set1 - set2:
                    if count1[c] == 1 :
                        return True
                return False
        #different by only by only one char

        if len(set1) - len(set2) == 1:
                # first case : increase the small set by one , decrease the big by one
                canSwap = any(True for c in set1 if count2[c] == 0 and count1[c] == 1)
                if canSwap:
                    for c in set2 - set1:
                        if count2[c] > 1 :
                            return True
                # second case : increase the small set by one , and keep the big with the same chars

                canSwap = any(True for c in set1 if count2[c] == 0 and count1[c] > 1)
                if canSwap:
                    for c in set2 & set1:
                        if count2[c] > 1:
                            return True
                # third case : decrease the big set and maintain the same length for the small set
                canSwap = any(True for c in set2 if count2[c] == 1 and count1[c] >= 1)
                if canSwap:
                    for c in set1-set2:
                        if count1[c] == 1:
                            return True
                return False

        #difference is zero


        if len(set1|set2) == len(set1) + len(set2) and len(set1) == len(set2) :
            if len(word1) == 1:
                return False
            return True
        return False
                            