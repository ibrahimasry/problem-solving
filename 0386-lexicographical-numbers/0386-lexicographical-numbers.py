class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        
        ans = [1]
        while len(ans) != n :
            curr = ans[-1] * 10
            while curr > n:
                curr //= 10
                curr += 1
                while curr % 10 == 0:
                    curr //= 10
            ans.append(curr)
            
            
        return ans