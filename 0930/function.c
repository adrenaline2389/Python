#include <stdio.h>

int plus (int a, int b)
{
    return a + b;
}

int factorial(int n)
{
    if (n == 1)
    {
        return n;
    }
    return n * factorial(n - 1);
}

int gcd(int a, int b)
{
    if (b == 0)
    {
        return a;
    }
    if (a < b)
    {
        return gcd(b, a);
    }
    if (a >= b)
    {
        return gcd(b, a % b);
    }
}

int main()
{
    int c;
    c = plus(6, 9);
    printf("%d\n", c);
    
    int a;
    a = factorial(4);
    printf("%d\n", a);

    int b;
    b = gcd(60, 18);
    printf("%d\n", b);

    return 0;

}

