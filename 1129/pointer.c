#include <stdio.h>

int f(char *s) {
    char *p = s;
    while (*p != '\0') p++;
    return p - s;
}

int main() {
    char s[80];
    int i;
    gets(s);
    i = f(s);
    printf("%d", i);
    return 0;
}