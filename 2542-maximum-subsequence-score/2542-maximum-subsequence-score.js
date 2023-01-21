/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @param {number} k
 * @return {number}
 */
const maxScore = function(nums1, nums2, k) {
    const  pq = new MinPriorityQueue()
    const n = nums1.length
    nums2 = nums2.map((v,i) => [v,i]).sort((a,b) => a[0]-b[0])
    for (let i = n - 1; i >= 0 && pq.size() + 1 < k; i--)
            pq.enqueue(nums1[nums2[i][1]])
    let j = n-k
    let s = pq.toArray().map(curr => curr.element).reduce((a,b) => a + b,0)
    let res = -Infinity
    while(j>=0){
        const [v,i] = nums2[j]
        s += nums1[i]
        pq.enqueue(nums1[i])
        res = Math.max(res, s * v)
        s -= pq.dequeue().element
        j -= 1
        
    }
    return res
    

};