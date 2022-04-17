using System;
namespace henhao
{
    public class Testing 
    {
        int _one;
        string _two;
        double _three;

        public Testing(int one, string two, double three)
        {
            _one = one;
            _two = two;
            _three = three;

        }

        public int One {
            get => _one;
            set => _one = value;
        }
        public string Two {
            get => _two;
            set => _two = value;
        }

        public double Three {
            get => _three;
            set => _three = value;
        }

        public virtual double Four{
            get => One * Three;

        }

        public override string ToString()
        {
            return base.ToString(); {
                return $"ur mum is gay";
            }
        }

        public string ToString(char format) {
            if ("B" == "B") {
                return $"";
            }
      
        }
    }

    public class TestingTwo : Testing
    {
        char _five;
        public TestingTwo(int one, string two, double three, char five) : base(one, two, three) {
            _five = five;
        }
        public override double Four {
            get => One * Three * Three;
        }
    }
}