



/**
 * Initialize your data structure here.
 */
var WordDictionary = function() {
    this.tri = {}
    
};

/**
 * Adds a word into the data structure. 
 * @param {string} word
 * @return {void}
 */
WordDictionary.prototype.addWord = function(word) {
    
    let tri = this.tri
    for(let c of word){
        if(c in tri) 
            tri = tri[c]
        else {
            tri[c] = {}
            tri = tri[c]
        }
        
    }
    
    tri["*"] = {}
    

    
};

/**
 * Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter. 
 * @param {string} word
 * @return {boolean}
 */
WordDictionary.prototype.search = function(word) {
    
    let tri = this.tri
    return helper(word, 0, tri)
    
};
function helper(word, start, tri){
        
    for(var i = start; i < word.length; i++){
        let c = word[i]
        if(c in tri) tri = tri[c]
       else if(c === "."){
            for(let l in tri){
              if(helper(word , i+1, tri[l]))
                     return true   
            }
               return false
       }
        else return false
        
    }
    if(tri["*"] === undefined) return false
     return true

}
/** 
 * Your WordDictionary object will be instantiated and called as such:
 * var obj = new WordDictionary()
 * obj.addWord(word)
 * var param_2 = obj.search(word)
 */