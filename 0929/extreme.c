#include <stdio.h>

int main()
{
    int array[5] = {};
    
    for (int i = 0; i < 5; i++)
    {
        scanf("%d", &array[i]);
    }

    for (int i = 0; i < 4; i++)
    {
        for (int j = 0; j < 4; j++)
        {
            if (array[j] > array[j + 1])
            {
                int temp = array[j];
                array[j] = array[j + 1];
                array[j + 1] = temp;
            }
        }
    }
    
    printf("MAX = %d\nmin = %d", array[4], array[0]);

    return 0;
}