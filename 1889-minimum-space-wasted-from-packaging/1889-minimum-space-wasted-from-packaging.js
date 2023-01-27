/**
 * @param {number[]} packages
 * @param {number[][]} boxes
 * @return {number}
 */
var minWastedSpace = function(packages, boxes) {
    packages.sort((a,b) => a - b)
    boxes.forEach(box => box.sort((a,b)=> a - b))
    const prefix = packages.reduce((acc,curr) => {
        acc.push(acc[acc.length -1] + curr)
        return acc
    },[0])
    let ans = Infinity
    for (let box of boxes){
        let start = 0
        let wasted = 0
        for (let size of box){
            let r = bs(packages,start, size)
            wasted += size * (r-start) - (prefix[r]-prefix[start])
            start = r
        }
        if (start == packages.length)
            ans = Math.min(wasted, ans) 
    }
    return ans == Infinity ? -1 : ans % (10**9 + 7)
    
    function bs(arr, start, target){
        let l = start
        let r = arr.length -1
        while (l<r){
            let m = Math.ceil((l+r)/2)
            if (arr[m] <= target)
                l = m
            else 
                r = m - 1
        }
        if(arr[l] <= target)
            return l + 1
        return l
    }
};