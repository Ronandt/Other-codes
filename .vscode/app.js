/*let user = {
    name: "John",
    sizes: {
      height: 182,
      width: 50
    }, ok: "test"
  };

let deepcopy = (object, copy = {}) => {
    for(let key in object) {
        typeof object[key] == "object" ? copy[key] = deepcopy(object[key]): copy[key] = object[key]
    }
    return copy;
}

let copy1 = deepcopy(user);
console.log(copy1)*/


/*let test = 'test';

function User(name) {
  this.name = name;
  this.age = 59

  this.sayHi = function() {
    console.log( "My name is: " + this.name );
    console.log(Symbol.toPrimitive)
  };
  [test]() {
    
  }

  this[Symbol.toPrimitive] = function(hint) { return hint == 'string' ? `Name: ${this.name}` : this.age }
}

let john = new User("John");

john.sayHi(); // My name is: John
console.log(+john)*/



/*let randomfunc = (min, max) => {
return Math.floor(Math.random() * (max - min + 1)) + min;

};
for(let i = 0; i < 101; i++){
console.log(randomfunc(3,5));
}*/

/*let maxsub=(arr)=>{let maximum=0,curr=0;for(let no of arr)maximum=Math.max(curr=Math.max(curr+=no,0),maximum);return maximum;}

console.log(maxsub([-1,2,3,-9]));

let maxsubReadable = (arr) => {
  let maximum = 0, curr = 0;
for (let no of arr) {
  curr += no;
  maximum = Math.max(curr, maximum);
  curr = Math.max(curr, 0);
}
return maximum;
}

console.log(maxsub([-1,2,3,-9]));
Math.sum()*/


let array = ['ok', 'o', 'a'];
console.log(array.filter((item, index, array) => item.includes('o')));







