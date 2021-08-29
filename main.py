#include<stdio.h>
int main()
{
    double celsius,farenheit;
    printf("Enter the  temperature in celsius :\n");
    scanf("%1f",&celsius);
    farenheit=((celsius*(9.0/5.0))+32);
    printf("%1f\n",farenheit);
    return 0;
    
}
