#include <stdio.h>

int main() {
    int n;
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        int spaces = (i > n / 2 && i < n - 1) ? -2 * i + 2 * (n - 1) - 1 : 2 * i - 1;
        if (i == n - 1 || i == 0) spaces = 0;
        if (spaces == 0) {
            for (int j = 0; j < n; j++) printf("*");
        } else {
            int stars = (n - spaces) / 2;
            for (int j = 0; j < stars; j++) printf("*");
            for (int j = 0; j < spaces; j++) printf(" ");
            for (int j = 0; j < stars; j++) printf("*");
        }
        printf("\n");
    }
    return 0;
}