class Solution:
    def maximumWhiteTiles(self, tiles: List[List[int]], carpetLen: int) -> int:
        tiles.sort()
        
        i = 0
        j = 0
        cover = 0
        res = 0
        n = len(tiles)
        while i < n and j < n:
            if tiles[j][0] + carpetLen > tiles[i][1]:
                cover = cover + (tiles[i][1] - tiles[i][0]) + 1
                i += 1
                res = max(cover, res)
            else:
                partial = max(0, tiles[j][0] + carpetLen - tiles[i][0] )
                res = max(cover + partial, res)

                cover -= (tiles[j][1] - tiles[j][0] + 1)
                j += 1
        return res