using System;
namespace TestConsoleApp {
    public abstract class Abstraction {
        public abstract void One();

        public virtual void Alright() {
            Console.WriteLine("Test");
        }
    }

    public class Child : Abstraction {
        private readonly Testings _testings; //if you use this, it is bad as it is not implmeneitng a concrete implenetation of a interface, rather a specific object that inherits from the interface, so if the name chantges etc it doen't matter
        private readonly IFuckMyself _Ifuckmyself; //this is better
        public Child(Testings testing) {
            _testings = testing;
        }
        public override void One()
        {
            throw new NotImplementedException();
        }
    }


    public interface IFuckMyself {
        public void Testing() {

        }
        //concrete methods only work when you strong type the variable of the interface when you instantiate the class 
        public void Oks();
    }

    public class Testings : IFuckMyself {
        //implmenet Ok
        public void Oks() {
//don't need override
        }
    }


}