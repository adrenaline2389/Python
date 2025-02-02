#include "stdio.h"

void yuan(char *s,char *s2)
{
    // int k = 0;
    // for(int i = 0;i < 81;i++){
    //     if(s[i] == 'a' || s[i] == 'e' || s[i] == 'i' || s[i] == 'o' || s[i] == 'u'
    //        || s[i] == 'A' || s[i] == 'E' || s[i] == 'I' || s[i] == 'O' || s[i] == 'U'){
    //         s2[k++] = s[i];
    //        }
    // }
    // s2[k] = '\0';
    while(*s!='\0')
    {
        if(*s=='a' ||*s=='o' ||*s=='e' ||*s=='i' ||*s=='u' ||
           *s=='A' ||*s=='O' ||*s=='E' ||*s=='I' ||*s=='U')
           {*s2=*s; s2++;}
        s++;
    }
    *s2='\0';
}

main()
{
    char str[81], str2[81];
    gets(str);
    yuan(str,str2);
    printf("%s", str2);
}
