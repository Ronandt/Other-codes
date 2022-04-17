using System;
using System.Collections.Generic;
using System.Text;
using henhao;

namespace TestConsoleApp
{

    public class Book
    {
        string _name, _author;
        int _pagecount;
        public Book(string name, string author, int pages) {
            
            _name = name;
            _author = author;
            _pagecount = pages;
        }

        public string GetDescription() {
            return _name;
        }

        
    } 
    
    class Being {
        string _name;
        int _age;

        public Being(string name, int age) {
            _name = name;
            _age = age;
        }

           public string Name {
            get => _name;
            set => _name = value;
        }

        public int Age {
            get => _age;
            set => _age = value;
        }

        public virtual int Multiply {
            get => _age *10;
        }
    }
    class Human : Being {

        double _dick_size;

        public Human(string name, int age , double dick_size) : base(name, age) {
            _dick_size = dick_size;

        }

     

        public double DickSize{
            get => _dick_size;
            set => value = _dick_size;
        }
        public string Test{
            get;set;
        }
        public override int Multiply {
            get => Age * 100;
        }
    }


    class Program
    {
        static void Main(string[] args)
        {
            Book variable = new Book("yes","ok",69);
            Book variable2 = new Book("yes","ok",69);
            int test = 3;
            object test2 = 3;
            StringBuilder yes = new StringBuilder();
            List<Array> a = new List<Array>();
     
            try{
                if (5 == 5) {
                    throw new ArgumentOutOfRangeException("x", "testing");
                }
                
            }
            catch (ArgumentOutOfRangeException e) {
                Console.WriteLine(e.Message);
            }
            finally {
                Console.WriteLine("YOur mum gay ");
                Console.WriteLine(String.Concat("dofsd", "jofdsjf"));
                Console.WriteLine(variable.Equals(variable));
                Console.WriteLine(variable.GetHashCode());
                Student testing = new Student();
                string bruh = testing.AdminNo;
                bruh ??= "this is null";
                Console.WriteLine(bruh);
                Console.WriteLine(testing.computeFinalMark());
                Console.WriteLine(Lecturer.test());
                Console.WriteLine((bool?)null);



            }

        }
    }
}
