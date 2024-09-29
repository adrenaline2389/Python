#include <stdio.h>

int main()
{
    int num, sum;

    num = 0;
    sum = 0;

    do
    {
        scanf("%d", &num);
        sum += num;
        printf("sum:%d\n", sum);
    }
    while (num != 0);

    return 0;    
}