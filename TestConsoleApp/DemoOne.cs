using System;
using System.Collections.Generic;
namespace TestConsoleApp {





    class Person {
        string _name;
        string _nric;
        public string Name {
            get => _name;
            set => _name = value;
        }

        public string Nric {
            get => _nric;
            set => _nric = value;
        }

        public void View() {
            Console.WriteLine($"Name: {_name}, Nric: {_nric}");
        }
    }

    class Student : Person {
        string _adminNo;
        double _testMark;
        double _examMark;

        public string AdminNo {
            get => _adminNo ?? "You have no current admin number";
            set => _adminNo = value;
        }

        public double TestMark {
            get => _testMark;
            set => _testMark = value;
        }

        public double ExamMark {
            get => _examMark;
            set => _examMark = value;
        }

        public double computeFinalMark() {
            return (ExamMark + TestMark)/2.0;
        }
    }

    class Lecturer : Person {
        string _staffId;
    
            double _totalTeachingHour;
    




    Dictionary<string, string> tests = new Dictionary<string,string>();
        public string StaffId {
            get => _staffId;
            set => _staffId = value;
        }

        public double TotalTeachingHour {
            get => _totalTeachingHour;
            set => _totalTeachingHour = value;

        }

        public double computeSalary() {
            return 90 * TotalTeachingHour;
        }

        public static double test() {
            return 4334.44;
        }

        public string this[string i] {
            get => tests[i];
            set => tests[i] = value;

        }
    }


}