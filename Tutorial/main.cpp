#include <iostream>
#include <cmath> //Math functions
#include <cs50>
using namespace std;


int get_int(int thing) {
int number;
printf("Enter a number");
scanf("%d", &number);
return number;
}




int main()
{
int ht;

do {
    ht = get_int("choose a height: ");
} while(ht < 1 || ht > 8);
    return 0;

}


