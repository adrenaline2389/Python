#include <stdio.h>
int a[16]={2, 3, 5, 7, 11, 13, 17, 23, 29, 31, 34, 71, 79, 97, 103};
void display()
{
    int i;
    for(i=0; i<16; i++) printf("%d ", a[i]);
}
int main()
{
    int n;
    scanf("%d", &n);
    a[15] = 0;

    for (int i = 14; i > -2; i--) {
        if (n < a[i]) {
            int temp = a[i];
            a[i] = a[i+1];
            a[i+1] = temp;
        }
        else {
            a[i+1] = n;
            break;
        }
    }
    display();
    return 0;
}