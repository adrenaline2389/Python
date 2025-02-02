#include <stdio.h>

void input(int a[])
{
    for (int i = 0; i < 10; i++) scanf("%d", &a[i]);
}

void swap(int a[])
{
    int min = a[0];
    for (int i = 1; i < 10; i++) {
        if (a[i] < min) min = a[i];
    }
    int index = 0;
    while (a[index] != min) index++;
    int temp = a[index];
    a[index] = a[0];
    a[0] = temp;

    int max = a[0];
    for (int i = 1; i < 10; i++) {
        if (a[i] > max) max = a[i];
    }
    index = 0;
    while (a[index] != max) index++;
    temp = a[index];
    a[index] = a[9];
    a[9] = temp;
}

void display(int a[])
{
    int i;
    for(i=0; i<10; i++)
        printf("%d\n", a[i]);
}

int main()
{
    int a[10];
    input(a);
    printf("input done\n");
    swap(a);
    printf("swap done\n");
    display(a);
    printf("display done\n");
    return 0;
}