#include <stdio.h>
#include <math.h>
int main()
{
    double d,p,r;
    scanf("%lf%lf%lf",&d,&p,&r);
    if(d==0)
        printf("0.0\n");
    else if((d*r-p)>=0)
        printf("God\n");
    else
    {   
        printf("%.1f", log(p/(p-d*r))/log(1+r));
    }
    return 0;
}