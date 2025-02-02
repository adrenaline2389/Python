#include <stdio.h>
#include <math.h>
int main() {
    int n;
    scanf("%d", &n);
    for (int i = 1 - n; i < n; i++) {
        int spaces = abs(i);
        int stars = (i <= 0) ? i + n : n - i;
        for (int j = 0; j < spaces; j++) printf(" ");
        for (int j = 0; j < stars; j++) printf("*");
        printf("\n");
    }
}