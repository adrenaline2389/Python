#include <stdio.h>
 
void average(double a[][5], int n)
{
    double sum=0.0;
    int i,j;
    for(i=0;i<n;i++)
    {
        sum=0;
        for(j=0;j<5;j++)
        {
            sum=sum+a[i][j];
        }
        printf("%.2lf ",sum/5.0);
    }
    printf("\n");
}
 
void average2(double a[][5], int n)
{
    double sum=0.0;
    int i,j;
    for(i=0;i<5;i++)
    {
        sum=0;
        for(j=0;j<n;j++)
        {
            sum=sum+a[j][i];
        }
        printf("%.2lf ",sum/10.0);
    }
    printf("\n");
}
 
void top(double a[][5], int n)
{
    double top;
    int i,j;
    for(i=0;i<5;i++)
    {
        top=a[j][i];
        for(j=0;j<n;j++)
        {
            if(a[j][i]>top)
            top=a[j][i];
        }
        printf("%.2lf ",top);
    }
}
 
int main()
{
    double a[10][5];
    int i, j;
    for(i=0; i<10; i++)
        for(j=0; j<5; j++)
            scanf("%lf", &a[i][j]);
    average(a,10);
    average2(a,10);
    top(a,10);
    return 0;
}