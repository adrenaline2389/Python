#include <stdio.h>
int main()
{
    int a, b, c;
    scanf("%d", &a);

    b = a / 100;
    c = a % 10;

    printf("%d\n%d", b, c);
    return 0;
}