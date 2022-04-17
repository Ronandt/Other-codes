const fs = require('fs') //to import
const name = require("./utils.js")
console.log("Notetaking app")
fs.writeFileSync('TestConsoleApp/nodejs/note.txt', 'I live in Pdelphia') //to write data
fs.appendFileSync('TestConsoleApp/nodejs/note.txt', "Testing")
console.log(name(3, 4));

