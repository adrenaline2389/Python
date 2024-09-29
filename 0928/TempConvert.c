#include <stdio.h>
int main()
{
    double f, c;

    scanf("%lf", &f);
    c = (f - 32) / 1.8;

    printf("%.2f", c);

    return 0;
}