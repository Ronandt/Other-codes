

    

    describe("pow", () => {
       
        let makeTestPower = () => {
            let one = Math.floor((Math.random() * 10) + 1), two = Math.floor((Math.random() * 10) + 1), three = one ** two;
            it(`${one} raised to power ${two} is ${three}`, () => { assert.equal(pow(one, two), three);})
            it(`This should be NaN`, () => {assert.isNaN(pow(-one, -two))}) 
        };

        for(let i = 0; i < 101; i++) makeTestPower() 

         });




