#include <stdio.h>

int main() {
    double x, y;
    scanf("%lf,%lf", &x, &y);

    if (x*x + y*y < 1 + 1e-3 && x*x + y*y > 1 - 1e-3) printf("Y");
    else printf("N");

    return 0;
}