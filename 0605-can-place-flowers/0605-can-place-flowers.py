class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        prev = 0
        for i in range(len(flowerbed)):
            if flowerbed[i]:
                prev = 1
            elif (i == len(flowerbed)-1 or not flowerbed[i+1]) and not prev:
                prev = 1
                n -= 1

            elif prev :
                prev = 0
        return n <= 0