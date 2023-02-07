/**
 * @param {number[]} fruits
 * @return {number}
 */
var totalFruit = function(fruits) {
        let  prev = curr = res = start = 0
        for (let i = 0; i < fruits.length; i++){
            if (fruits[i] == fruits[prev] || fruits[prev] == fruits[curr])
                [curr,prev] = [i,curr]
            else if(fruits[i] != fruits[prev] && fruits[i] != fruits[curr]){
                [curr,prev] = [i, curr]
                start = prev
            }
            res = Math.max((i - start) + 1, res)
        }
        return res

    
};