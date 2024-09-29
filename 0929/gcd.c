#include <stdio.h>
#include <stdlib.h>

int Gcd(int n, int m)    // 递归（欧几里得算法）
{
    if (n < 0 || m < 0)
    {
        printf("Invalid input: numbers should be non-negative.\n");
        exit (1);
    }

    if (m == 0)
        return n;
    
    if (m > n)
        return Gcd(m, n);
    
    return Gcd(m, n % m);
}

int main()  // 无论要执行什么操作，都要先调用主函数main()
{
    int m = 32;
    int n = 12;

    int result = Gcd(n, m);
    printf("GCD of %d and %d is: %d\n", n, m, result);

    return 0;

}