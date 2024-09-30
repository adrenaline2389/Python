#include <stdio.h>

// 第一题
int main()
{
    int a, b, c;
    scanf("%d",&a);
    scanf("%d",&b);
    scanf("%d",&c);

    if (a > b > c)
    {
        printf("max = %d\nmin = %d", a, c);
    }
    if (a > c > b)
    {
        printf("max = %d\nmin = %d", a, b);
    }
    if (b > a > c)
    {
        printf("max = %d\nmin = %d", b, c);
    }
    if (b > c > a)
    {
        printf("max = %d\nmin = %d", b, a);
    }
    if (c > b > a)
    {
        printf("max = %d\nmin = %d", c, a);
    }
    if (c > a > b)
    {
        printf("max = %d\nmin = %d", c, b);
    }
    return 0;
}


#include <stdio.h>

int main() {
    int a, b, c;
    // 输入三个整数
    scanf("%d", &a);
    scanf("%d", &b);
    scanf("%d", &c);

    int max, min;

    // 找最大值
    if (a > b) {
        if (a > c) {
            max = a;
        } else {
            max = c;
        }
    } else {
        if (b > c) {
            max = b;
        } else {
            max = c;
        }
    }

    // 找最小值
    if (a < b) {
        if (a < c) {
            min = a;
        } else {
            min = c;
        }
    } else {
        if (b < c) {
            min = b;
        } else {
            min = c;
        }
    }

    // 输出结果
    printf("max = %d\nmin = %d\n", max, min);
    return 0;
}
