#include <stdio.h>
#include <string.h>
#include <math.h>

int nL=0, nN=0;

int statistics(char *s)
{
    int n = 0;
    while (*s != '\0') {
        if (*s >= 'A' && *s <= 'Z' || *s >= 'a' && *s <= 'z') nL++;
        if (*s >= '0' && *s <= '9') nN++;
        if (*s == ' ') n++;
        *s++;
    }
    *s = '\0';
    return n;
}

int main()
{
    char s[81];
    int nS;
    gets(s);
    nS = statistics(s);

    printf("%d %d %d\n", nL, nN, nS);
    return 0;
}