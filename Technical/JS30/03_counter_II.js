var createCounter = function(init) {
    let count = init

    function increment() {
        count += 1
        return count
    }

    function decrement() {
        count -= 1
        return count
    }

    function reset() {
        count = init
        return count
    }

    return {
        increment,
        decrement,
        reset
    }
}