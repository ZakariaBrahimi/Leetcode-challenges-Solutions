/**
 * @param {string} ransomNote
 * @param {string} magazine
 * @return {boolean}
 */
var canConstruct = function(ransomNote, magazine) {
    const leters_counter = {}
    for(let i=0; i<magazine.length; i++){
        let letter = magazine[i]
        if (letter in leters_counter){
            leters_counter[letter] += 1
        }else{
            leters_counter[letter] = 0
        }
    }
    
    for (let letter of ransomNote){
        if (!leters_counter[letter]){
            return false
        }
        leters_counter[letter]--
    }
    return true
};

var canConstruct = function(ransomNote, magazine) {
    const map = {};
    for(let letter of magazine) {
        if (!map[letter]) {
            map[letter] = 0;
        }
        map[letter]++;
    }
    
    for(let letter of ransomNote) {
        if(!map[letter]) {
            return false;
        } 
        map[letter]--;
    }
    return true;
};