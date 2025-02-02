#include <stdio.h>

void removeSpace(char *s)
{
    int i=0,j=0;
    while(s[j]!='\0')
    {
        if(s[j]==' ') j++;
        else
            s[i++]=s[j++];
    }
    s[i]='\0';
}

int main()
{
    char s[81];
    gets(s);
    removeSpace(s);
    printf("%s", s);
    return 0;
}