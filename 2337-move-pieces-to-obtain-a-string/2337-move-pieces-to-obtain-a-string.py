class Solution:
    def canChange(self, start: str, target: str) -> bool:
        
        i = 0
        j = 0
        countS = Counter(start)
        countT = Counter(target)
        if countS["L"] != countT["L"]:
            return False
        if  countS["R"] != countT["R"]:
            return False
        n = len(start)
        space = 0
        while i < n and j < n :
            
            if start[i] == "_":
                i += 1
                space += 1
            elif target[j] == "_":
                j += 1
            elif target[j] != start[i]:
                return False
            elif start[i] == "R":
                space = 0
                i += 1
                j += 1
                continue
            elif i < j:
                print(i)
                return False
            elif space < j-i:
                return False
            else:
                j += 1
                i += 1
        n = len(start)
        space = 0
        i = n-1
        j = n-1

        while i >=0 and j >=0 :
            
            if start[i] == "_":
                i -= 1
                space += 1
            elif target[j] == "_":
                j -= 1
            elif target[j] != start[i]:
                return False
            elif start[i] == "L":
                space = 0
                i -=1
                j -=1
                continue
            elif i > j:
                return False
            elif space < j-i:
                return False
            else:
                i -= 1
                j -= 1
        return True

                    
                    