/**
 * @param {character[][]} seats
 * @return {number}
 */
var maxStudents = function(seats) {
    
 let m = seats[0].length
 let n = seats.length
 const  recurse = (pos, currRow, prevRow , cache) => {
            if (pos == n * m) return 0
            let key = `${pos} - ${currRow} - ${prevRow}`
            if (key in cache) return cache[key]
            let i = Math.floor(pos / m)
            let j = pos % m
            if (j == 0){
                prevRow = currRow
                currRow = 0
            }
            let ans = 0
            let t = seats[i][j]


            ans = recurse(pos + 1, currRow, prevRow, cache)
            if (t == "."){
             let  l = tl = tr = true

                if (j != 0){
                    l = ((currRow & (1 << (j-1))) == 0)
                    tl = ((prevRow & (1 << (j-1))) == 0)
                }
                if (j != m - 1)
                    tr = ((prevRow & (1 << (j+1))) == 0)
                if (l && tr && tl) 
                    ans = Math.max(ans, 1 + recurse(pos + 1, currRow | (1 << j) , prevRow, cache))
            }
            cache[key] = ans
            return ans
 }
        return recurse(0,0,0, {})
                

    
};