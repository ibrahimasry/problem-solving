class Solution:
    def strongPasswordChecker(self, s: str) -> int:
        missing = 0
        
        missing += 0 if  any(c.isupper() for c in s) else 1
        missing += 0 if  any(c.islower() for c in s) else 1
        missing += 0 if  any(c.isdigit() for c in s) else 1
        
        n = len(s)
        
        if n < 6:
            return max(6-n, missing)
        
        changes = 0
        i = 2
        removeOne = 0
        removeTwo = 0
        while i < n:
            
            if s[i] == s[i-1] == s[i-2]:
                count = 2
                while i < n and s[i] == s[i-1]:
                    i += 1
                    count += 1 
                changes += count//3
                if count % 3 == 0:
                    removeOne += 1
                if count % 3 == 1:
                    removeTwo += 1
            else :
                i += 1
        if n <= 20 :
            return max(changes, missing)
        toDelete = n - 20
        changes -= min(removeOne, toDelete)
        changes -= min(max(toDelete-removeOne, 0), removeTwo * 2) // 2
        changes -= max(toDelete - removeOne - removeTwo * 2, 0) // 3
        return toDelete + max(changes, missing)