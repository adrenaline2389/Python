#include <stdio.h>

double fib(int n) {
    double a1 = 1, a2 = 1, next;
    if (n == 1 || n == 2) return 1;
    for (int i = 2; i < n; i++) {
        next = a1 + a2;
        a1 = a2;
        a2 = next;
    }
    return next;
}

double sum(int n) {
    double s = 0;
    for (int i = 2; i < n + 2; i++) {
        double up = fib(i+1), down = fib(i);
        double an = up / down;
        s += an;
    }
    return s;
}

int main() {
    int n;
    double ans;
    scanf("%d", &n);
    ans = sum(n);
    printf("%.4lf", ans);

    return 0;
}