#include <bits/stdc++.h>
using namespace std;

int FlagMatrix[100][100];
char SplithunnyMatrix[100][100];
int  HGroupCounter = 0;
int r,c;

void ClearMatrix()
{
    int i,j ;
  for (i = 0; i <r ; i++)
  {
    for (j = 0; j <c ; j++)
    {
    FlagMatrix[i][j] = 0;

     }
   }
}
int FindFirstH()
{
int i,j ;
  ClearMatrix();
  for ( i = 0; i <r ; i++)
  {
    for ( j = 0; j <c ; j++)
    {
      if (SplithunnyMatrix[i][j] == 'H')
      {
        FlagMatrix[i][j] =1;
        return 1;

      }
     }
   }
  return 0;
}
int FindNextH(){
    int i,j ;
  for ( i = 0; i <r ; i++)
  {
    for ( j = 0; j <c ; j++)
    {
      if (FlagMatrix[i][j] == 1)
      {
        if (i >= 1 && SplithunnyMatrix [i-1][j] == 'H' && FlagMatrix [i-1][j] != 1)
        {
          FlagMatrix [i-1][j] = 1;
          return 1;
        }
        if (j >= 1 && SplithunnyMatrix[i][j-1] == 'H' && FlagMatrix [i][j-1] != 1)
        {
          FlagMatrix [i][j-1] = 1;
          return 1;
        }
        if (i<r-1 && SplithunnyMatrix[i+1][j] == 'H' && FlagMatrix [i+1][j] != 1)
        {
          FlagMatrix [i+1][j] = 1;
          return 1;
        }
        if (j < c-1 && SplithunnyMatrix[i][j+1] == 'H' && FlagMatrix [i][j+1] != 1)
        {
          FlagMatrix [i][j+1] = 1;
          return 1;
        }
      }
     }
   }
   return 0;

}
void ReplaceHInMatrix()
{
    int i,j ;
  for ( i = 0; i <r ; i++)
  {
    for ( j = 0; j <c ; j++)
    {
      if (FlagMatrix[i][j] == 1)
      {
        SplithunnyMatrix[i][j] = '.';
      }
    }
  }
}

int main() {
    int i,j ;
   cin >> r >> c;
   for ( i = 0; i <r ; i++)
   {
     for ( j = 0; j <c ; j++)
     {
     cin >> SplithunnyMatrix[i][j];

     }
   }

   while (FindFirstH() == 1)
  {
    HGroupCounter +=1;
    while (FindNextH() == 1)
    {

    }

  ReplaceHInMatrix();

  }
   cout << "Oh, bother. There are "<< HGroupCounter << " pools of hunny." ;
}
