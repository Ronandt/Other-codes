
describe("powpow", () => 
{
    

    describe("pow", () => {
       
        let makeTestPower = () => {
            let one = Math.floor((Math.random() * 10) + 1), two = Math.floor((Math.random() * 10) + 1), three = one ** two;
            let random_list = [ it(`${one} raised to power ${two} is ${three}`, () => { assert.equal(pow(one, two), three);}),  it(`This should be NaN`, () => {assert.isNaN(pow(-one, -two))}) 
        ]
        console.log(random_list[Math.floor(Math.random() * random_list.length)]);
        console.log('a');
        return random_list[random_list.length - 1];
            

        };

        for(let i = 0; i < 101; i++) makeTestPower() 

         });





})
