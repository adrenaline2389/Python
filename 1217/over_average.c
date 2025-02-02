#include <stdio.h>

int main() {
    int a[10];
    int sum = 0;
    for (int i = 0; i < 10; i++) {
        scanf("%d", &a[i]);
        sum += a[i];
    }
    float ave = sum / 10.;
    int ans = 0;
    for (int i = 0; i < 10; i++) {
        if (a[i] > ave) ans++;
    }
    printf("%d", ans);

    return 0;
}