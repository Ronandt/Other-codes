#include <iostream>

using namespace std;

void testing()
{
    int testing;
    cout << testing << endl;
};



class Book
{
private:

public:
    string title;
    string author;
    string a;
    int pages;
    double b;

    Book() {
        a = "no title";
        b = 69;
    };

    Book(string material, double weight) {
        setMaterial(material);
       b = weight;
    cout << material << weight << endl;
    };

    void setMatrial(string materials) {
        if (materials == "paper" || materials == "wood") {a = materials;}
        else {a = "NoneMaterial";}

    }



    bool Fat() {
        return b > 60; };

};


int main()
{
    int guess;
    int secret = 3;
    int guessCount = -1;
    do {
        guessCount++;

        cout << "Guess the number: ";
        cin >> guess;

    } while (guess != secret);

string yes = "thing";
string *pyes = &yes;
    int numberGrid[2][2] = {{1,2}, {3,4}};
    for(int i = 0; i < 2; i++) {
        cout << numberGrid[i][i % 1] << "\n" << numberGrid[i][(i % 1) + 1] << "\n";

    }

    cout << &numberGrid << "\n"; //print out memeory address aka pointer
    cout << pyes << "\n";
    cout << *pyes << "\n";
    cout << *&yes << "\n";

    Book book1("paper", 30);

    book1.title = "Harry Potter";
    book1.author = "JK Rowling";
    book1.pages = 324;
    Book book3;
    cout << book1.Fat() << endl;


    cout << book1.pages << endl;


    int thing[] = {3,1,6,4};
    cout << (thing + 1) << endl;





    return 0;
};
