#include <stdio.h>

void binary(int n) {
    int bin[32];
    int index = 0;

    if (n == 0) {
        printf("0");
        return;
    }

    while (n != 0) {
        bin[index++] = n % 2;
        n /= 2;
    }

    for (int i = index - 1; i >= 0; i--) printf("%d", bin[i]);
}

int main() {
    int n;
    scanf("%d", &n);
    binary(n);
    return 0;
}