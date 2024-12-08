const hourRegex = /(?:\b([2][0-3]|0?\d|1[0-9]):([0-5][0-9])(?::([0-5][0-9]))?)(?:\n|$)/

console.log(hourRegex.test("23:50:32"))
console.log(hourRegex.test("23:60"))
console.log(hourRegex.exec("23:50:32"))
console.log("23:50:32".match(hourRegex))