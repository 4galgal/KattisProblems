#include <stdio.h>

int main(void){
int i;
int n;
int number;

int ignore=scanf("%d", &n);

ignore=scanf("%d", &number);
int max=number;
//printf("the first max is %d\n", max);
for(i=0; i<n-1; i++){
   ignore=scanf("%d", &number);
   if (number > max){
   // printf("the new max is %d\n", number);
       max= number;
   }
    
}

printf("%d\n", max);

}


//in kattis you need to add variable=scanf(...) to avoid warnings about unused return value
//you can not use scanf without assigning it to a variable otherswise it gives a compilation warning
//to create long long int: long long int var;
//#the problem was that the max input included the firs line which is n

