#include <stdio.h>
#include <stdlib.h>
int main()
{
    int a[50][50];
    int M,N,m,n,i,j;
    scanf("%d%d", &M, &N);
    i=1; j=M*N;
    for(m=0; m<M; m++)
    {
/*********** error **************
        for(n=0; n<N/2; n++)
            a[m][n]=i++;
        for(n=0; n<N/2; n++)
            a[m][N-1-n]=j--;
*********************************/
        for(n=0; n<N/2; n++) {
            if (m % 2 == 0) {
                a[m][n] = i++;
            } else {
                a[m][N/2-1-n] = i++;
            }
        }
        for(n=0; n<N/2; n++) {
            if (m % 2 == 0) {
                a[m][N-1-n] = j--;
            } else {
                a[m][N/2+n] = j--;
            }
        }

    }
    for(m=0; m<M; m++)
    {
        for(n=0; n<N; n++)
            printf("%2d ", a[m][n]);
        printf("\n");
    }
    return 0;
}