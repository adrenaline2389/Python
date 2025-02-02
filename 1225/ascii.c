#include <stdio.h>

int sum(char *s)
{
    int t=0,i=0;
    while(s[i] != '\0')
        t += s[i++];
    return t;
}
int main()
{
    char s1[81], s2[82];
    gets(s1);
    gets(s2);
    printf("%d", sum(s1) - sum(s2));
   return 0;
}