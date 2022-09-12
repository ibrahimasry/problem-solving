
var DetectSquares = function() {
    this.hash = {}
};

/** 
 * @param {number[]} point
 * @return {void}
 */
DetectSquares.prototype.add = function(point) {
    let str = point[0] + "-" + point[1]
    let map = this.hash
    map[str] = (map[str] || 0) + 1
};

/** 
 * @param {number[]} point
 * @return {number}
 */
DetectSquares.prototype.count = function(point) {
     let [x, y]  = point
    let map = this.hash
    let count = 0
    for(let key in map){
        let [x1, y1] = key.split("-")
        x1 = +x1
        y1 = +y1
        if(Math.abs(x - x1) == 0 || Math.abs(y1 - y) !== Math.abs(x1 - x)) continue
        let first = map[x + "-" + y1] || 0
        let second = map[x1 + "-" + y] || 0
        count += first * second * map[key]
    }
    
    

    return count

};

/** 
 * Your DetectSquares object will be instantiated and called as such:
 * var obj = new DetectSquares()
 * obj.add(point)
 * var param_2 = obj.count(point)
 */