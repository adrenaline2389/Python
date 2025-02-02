#include <stdio.h>

int main() {
    double h = 100, d = 100, cur = 100;
    int n;
    scanf("%d", &n);

    for(int i = 0; i < n; i++) {
        h /= 2;
        if (i != 0) {
            d += cur;
            cur /= 2;
        }
    }
    printf("%.3lf %.3lf", d, h);
}