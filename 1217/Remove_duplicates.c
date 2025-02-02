#include <stdio.h>

int main() {
    int a[10] = {0}, vis[8964] = {0}, i;
    for (i = 0; i < 10; i++) {
        scanf("%d", &a[i]);
        if (vis[a[i]] == 0) {
            printf("%d\n", a[i]);
            vis[a[i]] = 1;
        }
    }
    return 0;
}