#include <stdio.h>

int main() {
    int a, b, c;
    scanf("%d:%d:%d", &a, &b, &c);

    c += 20;
    if (c >= 60) {
        c -= 60;
        b += 1;
    }

    if (b >= 60) {
        b -= 60;
        a += 1;
    }

    if (a >= 24) {
        a -= 24;
    }

    printf("%02d:%02d:%02d\n", a, b, c);

    return 0;
}
