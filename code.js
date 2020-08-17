// Binary constants:

let myBinary = 0b101; // 101 binary is 5 decimal

// Converting a binary string to a Number

let myValue1 = Number("0b101");

// or

let myValue2 = parseInt("101", 2); // base 2

// All these print 5:
console.log(myBinary); // 5
console.log(myValue1); // 5
console.log(myValue2); // 5

// Decimal constants (just like normal)

const val = 123;

// Converting a decimal to a binary string

const binVal = val.toString(2); // convert to base 2 number string

console.log(`${val} decimal is ${binVal} in binary`);
