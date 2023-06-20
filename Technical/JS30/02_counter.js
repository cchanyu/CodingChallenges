var createCounter = function(n) {
    let count = n || 0;
    return function() {
        let result = count;
        count++;
        return result;
    }
}