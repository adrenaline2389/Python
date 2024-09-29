#include <stdio.h>
#define PI 3.14159

int main()
{
    double r;
    double s;

    scanf("%lf", &r);
    s = PI * r * r;
    printf("%.2f", s);

    return 0;

}