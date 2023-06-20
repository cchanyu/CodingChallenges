function map(arr, fn) {
    const result = [];

    for (let i = 0; i < arr.length; i++) {
        const transformed = fn(arr[i], i);
        result.push(transformed)
    }

    return result;
}