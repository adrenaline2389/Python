#include <stdio.h>

int main()
{
    int n;
    printf("Enter the size of the array: ");
    scanf("%d", &n);

    int array[n];
    int max, min;

    // 输入数组
    printf("Enter the elements of the array: \n");
    for (int i = 0; i < n; i++)
    {
        scanf("%d", &array[i]);
    }

    // 初始化最大值和最小值
    max = array[0];
    min = array[0];

    // 遍历数组，查找最大值和最小值
    for (int i = 1; i < n; i++)
    {
        if (array[i] > max)
        {
            max = array[i];
        }
        if (array[i] < min)
        {
            min = array[i];
        }
    }

    printf("MAX = %d\nmin = %d", max, min);

    return 0;
}
