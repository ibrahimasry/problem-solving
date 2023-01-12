class Solution:
    def makeSimilar(self, nums: List[int], target: List[int]) -> int:
        odds1 = sorted([n for n in nums if n %2])   
        odds2 = sorted([n for n in target if n %2])

        evens1 = sorted([n for n in nums if n % 2 == 0])
        evens2 = sorted([n for n in target if n % 2 == 0])

        def makeEqual(arr1,arr2):
            res = 0
            for c1,c2 in zip(arr1,arr2):
                res += abs(c1-c2) // 2 
            return res 
        
        return makeEqual(odds1,odds2) + makeEqual(evens1,evens2) >> 1