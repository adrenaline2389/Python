#include <stdio.h>

int main() {
    int n;
    scanf("%d", &n);
    float sum = 6;
    for (int i = 0; i < n; i++) {
        int num;
        float price;
        scanf("%f %d", &price, &num);
        sum += num * price;
    }
    if (sum >= 105) sum -= 6;
    printf("%.2f", sum);
    return 0;
}