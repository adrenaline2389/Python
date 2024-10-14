#include <stdio.h>

int main() {
    int n;  // 菱形的最大宽度
    int i, j;

    scanf("%d", &n);

    // 打印上半部分
    for(i = 1; i <= n / 2 + 1; i++) {
        // 打印空格
        for(j = i; j < n / 2 + 1; j++) {
            printf(" ");
        }
        // 打印星号
        for(j = 1; j <= 2 * i - 1; j++) {
            printf("*");
        }
        printf("\n");
    }

    // 打印下半部分
    for(i = n / 2; i >= 1; i--) {
        // 打印空格
        for(j = n / 2 + 1; j > i; j--) {
            printf(" ");
        }
        // 打印星号
        for(j = 1; j <= 2 * i - 1; j++) {
            printf("*");
        }
        printf("\n");
    }

    return 0;
}
